# Copyright (c) 2018 David Chan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from searchlet import Environment, Action, State
from searchlet.ds import Stack
from .SearchAlgorithm import SearchAlgorithm
from typing import Tuple, List, Union, Optional
import math


class DepthLimitedDFS(SearchAlgorithm):

    @classmethod
    def solve(cls, environment: Environment, start: State, goal: Union[List[State], State], *args, **kwargs) -> Tuple[Optional[List[Tuple[State, Optional[Action]]]], Union[float, int]]:
        """Solve a problem using depth-limited first search
        
        :param environment: The environment
        :type environment: Environment
        :param start: The starting state
        :type start: State
        :param goal: The goal state
        :type goal: Union[List[State], State]
        :return: The solution, or None if not found
        :rtype: Tuple[List[Action], Union[float, int]]
        """

        # Define the goal test - the reason that we need to 
        # do this is if the goal is a set of goals, and not just
        # a single element. If it is a single element, then we just
        # return current == goal, however a list needs to be checked
        # for each of the goal elements
        if type(goal) == list:
            def goal_test(current: State, goals: List[State]) -> bool:
                for goal in goals:
                    if current == goal:
                        return True
                return False
        else:
            def goal_test(current: State, goal: State) -> bool:
                return current == goal

        # Handle the depth limit of the algorithm
        if 'depth_limit' not in kwargs:
            # We have full DFS
            depth_limit = math.inf
        else:
            depth_limit = kwargs['depth_limit']

        # Define the open-list and the parent map
        open_list = Stack()
        parent_map = {}
        max_depth = 0

        # Add the start state to the open list
        open_list.push((start, 0))

        while not open_list.empty():
            # Pop the current element from the open list
            current_state, current_depth = open_list.pop()
            if current_depth >= depth_limit:
                continue

            # Handle the maximum depth
            max_depth = max(max_depth, current_depth)

            # Check if the current state is the goal
            if goal_test(current_state, goal):
                # Then we know that we've done it!
                # We need to break
                break
                
            # Generate the next set of possible states and add them to
            # the open list
            for possible_action in environment.get_actions(current_state):
                # Generate
                next_state = environment.apply_action(possible_action, current_state)[0]

                if next_state not in parent_map:
                    parent_map[next_state] = (current_state, possible_action)
                # Add to open list
                open_list.push((next_state, current_depth + 1))

        if goal_test(current_state, goal):
            # We found the goal!
            # Now we need to extract the proper state
            state_actions: List[Tuple[State, Optional[Action]]] = []
            state_actions.append((current_state, None))
            while current_state != start:
                current_state, action = parent_map[current_state]
                state_actions.append((current_state, action))
            return ((list(reversed(state_actions)), len(state_actions)))

        # Determine if we died because of a lack of states, or a depth limit
        if max_depth < depth_limit:
            # We died because we ran out of paths
            return (None, -2)
        else:
            return (None, -1)


class DFS(SearchAlgorithm):

    @classmethod
    def solve(cls, environment: Environment, start: State, goal: Union[List[State], State], *args, **kwargs) -> Tuple[Optional[List[Tuple[State, Optional[Action]]]], Union[float, int]]:
        """Solve a problem using depth first search
        
        [description]
        
        :param environment: The environment
        :type environment: Environment
        :param start: The starting state
        :type start: State
        :param goal: The goal state
        :type goal: Union[List[State], State]
        :return: The solution, or None if not found
        :rtype: Tuple[List[Action], Union[float, int]]
        """

        # Define the goal test - the reason that we need to 
        # do this is if the goal is a set of goals, and not just
        # a single element. If it is a single element, then we just
        # return current == goal, however a list needs to be checked
        # for each of the goal elements
        if type(goal) == list:
            def goal_test(current: State, goals: List[State]) -> bool:
                for goal in goals:
                    if current == goal:
                        return True
                return False
        else:
            def goal_test(current: State, goal: State) -> bool:
                return current == goal

        # Define the open-list and the parent map
        open_list = Stack()
        parent_map = {}
        closed_list = set()

        # Add the start state to the open list
        open_list.push(start)

        while not open_list.empty():
            # Pop the current element from the open list
            current_state = open_list.pop()
            if current_state in closed_list:
                continue
            else:
                closed_list.add(current_state)

            # Check if the current state is the goal
            if goal_test(current_state, goal):
                # Then we know that we've done it!
                # We need to break
                break
                
            # Generate the next set of possible states and add them to
            # the open list
            for possible_action in environment.get_actions(current_state):
                # Generate
                next_state = environment.apply_action(possible_action, current_state)[0]

                if next_state not in parent_map:
                    parent_map[next_state] = (current_state, possible_action)
                # Add to open list
                open_list.push(next_state)

        if goal_test(current_state, goal):
            # We found the goal!
            # Now we need to extract the proper state
            state_actions: List[Tuple[State, Optional[Action]]] = []
            state_actions.append((current_state, None))
            while current_state != start:
                current_state, action = parent_map[current_state]
                state_actions.append((current_state, action))
            return ((list(reversed(state_actions)), len(state_actions)))

        return (None, -1)