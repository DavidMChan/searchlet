# Copyright (c) 2018 David Chan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


from abc import ABC, abstractclassmethod
from typing import List, Tuple


class Action(ABC):
    """
    Abstract base class representing an action type. Primarily
    for typing, as actions are traditionally handled on an 
    environment by environment basis.
    """

    def __init__(self, ) -> None:
        pass


class ReverseAction(Action):
    """
    Abstract base class representing a reverse action. In general, the
    reverse action is an action which when applied, undoes an action
    which was generated earlier. This is one of the faster ways
    to handle traversing a search space
    """

    def __init__(self, ) -> None:
        pass


class Environment(ABC):
    """
    Abstract base class representing a search environment. This
    is a key part of a search problem, which we can solve using
    other methods in the library
    """

    def __init__(self, ) -> None:
        pass

    @abstractclassmethod
    def get_actions(self, ) -> List[Action]:
        raise NotImplementedError("Environments must have a get_actions method.")

    @abstractclassmethod
    def apply_action(self, action: Action) -> Tuple[Environment, ReverseAction]:  # noqa: F821
        raise NotImplementedError("Environments must have an apply_action method.")

    @abstractclassmethod
    def is_goal(self,) -> bool:
        raise NotImplementedError("No goal-test implemented.")


class WeightedEnvironment(Environment):
    """
    Abstract class representing a weighted environment. In these environments
    we have additional edge-cost parameters, which are not necessarily present 
    in the traditional search environment.
    """

    def __init__(self, ) -> None:
        pass

    @abstractclassmethod
    def get_value(self, ) -> float:
        raise NotImplementedError("No get_value method defined in a weighted edge-cost environment")

    @abstractclassmethod
    def get_cost(self, action: Action) -> float:
        raise NotImplementedError("No get_cost method defined in a weighted edge-cost environment.")
