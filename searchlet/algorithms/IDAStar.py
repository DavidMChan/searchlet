# Copyright (c) 2018 David Chan
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import queue
import math

from .SearchAlgorithm import WeightedSearchAlgorithm
from searchlet import WeightedEnvironment, Action, State
from searchlet.ds import PriorityQueue
from typing import Union, List, Tuple, Optional, Callable


class IDAStar(WeightedSearchAlgorithm):

    @classmethod
    def _bounded_astar_solve(cls,
                             environment: WeightedEnvironment,
                             start: State,
                             goal: State,
                             heuristic: Callable[[State, State], Union[float, int]],
                             f_cost_bound: Union[float, int]) -> Tuple[Optional[List[Tuple[State, Optional[Action]]]], Union[float, int]]:

        # Initialize some variables
        open_list = PriorityQueue()
        closed_list = {}
        parent_map = {}

        # Add the start state to the queue
        open_list.push((start, 0), 0 + heuristic(start, goal))

        min_over_f_cost = math.inf

        # Main Loop
        while not open_list.empty():

            # Pop the lowest f-cost element from the queue
            f_cost, (current_state, g_cost) = open_list.pop()

            if f_cost > f_cost_bound:
                min_over_f_cost = min(f_cost, min_over_f_cost)
                continue

            # Check to see if this is the goal
            if current_state == goal:
                # We're done!
                break

            # If this is not the goal, expand the neighbor nodes
            for action in environment.get_actions(current_state):
                # Get the next state
                next_state = environment.apply_action(action, current_state)[0]

                # Get the cost of the next state
                cost = environment.get_cost(action, current_state)

                # Compute the f_cost of the new state
                new_f_cost = g_cost + cost + heuristic(next_state, goal)

                if next_state not in closed_list or closed_list[next_state] > new_f_cost:
                    # Add it to the priority queue and parent map
                    # the priority queue implementation will not update unless it has to
                    return_value = open_list.push(
                        (next_state, g_cost + cost), priority=new_f_cost)
                    if return_value == PriorityQueue.NONEXIST or return_value == PriorityQueue.EXISTS_UPDATED:
                        # Only add to the parent map if our way is better
                        parent_map[next_state] = (current_state, action, cost)

            # Add the element to the closed list
            closed_list[current_state] = f_cost

        if current_state == goal:
            # We solved the problem!
            total_cost = 0
            state_action_pairs = []
            state_action_pairs.append((current_state, None))
            while current_state != start:
                current_state, action, cost = parent_map[current_state]
                total_cost += cost
                state_action_pairs.append((current_state, action))

            return (list(reversed(state_action_pairs)), total_cost)

        return (None, min_over_f_cost)

    @classmethod
    def solve(cls,
              environment: WeightedEnvironment,
              start: State,
              goal: State,
              *args,
              **kwargs) -> Tuple[Optional[List[Tuple[State, Optional[Action]]]], Union[float, int]]:

        # Handle the heuristic function
        if 'heuristic' in kwargs and kwargs['heuristic'] is not None:
                h_function = kwargs['heuristic']
        else:
            def h_function(x: State, y: State) -> Union[float, int]:
                return 0

        # Main solution loop
        heuristic_start_bound = h_function(start, goal)
        while True:
            path = IDAStar._bounded_astar_solve(
                environment, start, goal, h_function, heuristic_start_bound)
            if path[0] is None:
                heuristic_start_bound = path[1]
            else:
                return path
