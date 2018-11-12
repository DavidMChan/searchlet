# Copyright (c) 2018 David Chan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from abc import ABC, abstractclassmethod
from searchlet import Environment, Action, State, WeightedEnvironment
from typing import Tuple, List, Union, Optional


class SearchAlgorithm(ABC):

    @abstractclassmethod
    def solve(cls, environment: Environment, start: State, goal: Union[List[State], State], *args, **kwargs) -> Tuple[Optional[List[Tuple[State, Optional[Action]]]], Union[float, int]]:
        raise NotImplementedError("Search algorithms should have a solve method")


class WeightedSearchAlgorithm(ABC):

    @abstractclassmethod
    def solve(cls, environment: WeightedEnvironment, start: State, goal: State, *args, **kwargs) -> Tuple[Optional[List[Tuple[State, Optional[Action]]]], Union[float, int]]:
        raise NotImplementedError("Search algorithms should have a solve method")