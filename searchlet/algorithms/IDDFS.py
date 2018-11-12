# Copyright (c) 2018 David Chan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from searchlet import Environment, Action, State
from .SearchAlgorithm import SearchAlgorithm
from .DFS import DepthLimitedDFS
from typing import Tuple, List, Union, Optional
import math


class IDDFS(SearchAlgorithm):

    @classmethod
    def solve(cls, environment: Environment, start: State, goal: Union[List[State], State], *args, **kwargs) -> Tuple[Optional[List[Tuple[State, Optional[Action]]]], Union[float, int]]:
        """Solve a problem using iterative-deepening depth-limited depth first search
        
        :param environment: The environment
        :type environment: Environment
        :param start: The starting state
        :type start: State
        :param goal: The goal state
        :type goal: Union[List[State], State]
        :param max_depth: The maximum depth of the IDDFS search
        :type max_depth: int
        :return: The solution, or None if not found
        :rtype: Tuple[List[Action], Union[float, int]]
        """

        # Handle the maximum depth parameter
        if 'max_depth' in kwargs:
            max_depth = kwargs['max_depth']
        else:
            max_depth = math.inf

        depth = 0
        while depth < max_depth:
            depth += 1
            path = DepthLimitedDFS.solve(environment, start, goal, depth_limit=depth, *args, **kwargs)
            if path[0] is None and path[1] == -1:
                return path
            elif path[0] is not None:
                return path
class IDDFS(SearchAlgorithm):

    @classmethod
    def solve(cls, environment: Environment, start: State, goal: Union[List[State], State], *args, **kwargs) -> Tuple[Optional[List[Tuple[State, Optional[Action]]]], Union[float, int]]:
        """Solve a problem using iterative-deepening depth-limited depth first search
        
        :param environment: The environment
        :type environment: Environment
        :param start: The starting state
        :type start: State
        :param goal: The goal state
        :type goal: Union[List[State], State]
        :param max_depth: The maximum depth of the IDDFS search
        :type max_depth: int
        :return: The solution, or None if not found
        :rtype: Tuple[List[Action], Union[float, int]]
        """

        # Handle the maximum depth parameter
        if 'max_depth' in kwargs:
            max_depth = kwargs['max_depth']
        else:
            max_depth = math.inf

        depth = 0
        while depth < max_depth:
            depth += 1
            path = DepthLimitedDFS.solve(environment, start, goal, depth_limit=depth, *args, **kwargs)
            if path[0] is None and path[1] == -1:
                return path
            elif path[0] is not None:
                return path