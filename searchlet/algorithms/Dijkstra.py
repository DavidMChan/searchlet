# Copyright (c) 2018 David Chan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from searchlet import Action, State, WeightedEnvironment
from .SearchAlgorithm import WeightedSearchAlgorithm
from .AStar import AStar
from typing import Tuple, List, Union, Optional


class Dijkstra(WeightedSearchAlgorithm):

    @classmethod
    def solve(cls, environment: WeightedEnvironment, start: State, goal: Union[List[State], State], *args, **kwargs) -> Tuple[Optional[List[Tuple[State, Optional[Action]]]], Union[float, int]]:
        """Solve a problem using Dijkstra's algorithm
        
        :param environment: The environment
        :type environment: Environment
        :param start: The starting state
        :type start: State
        :param goal: The goal state
        :type goal: Union[List[State], State]
        :return: The solution, or None if not found
        :rtype: Tuple[List[Action], Union[float, int]]
        """

        return AStar.solve(environment, start, goal, heuristic=None, *args, **kwargs)