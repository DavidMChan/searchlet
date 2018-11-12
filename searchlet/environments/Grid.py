# Copyright (c) 2018 David Chan
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import List, Tuple, Optional, cast
from enum import Enum
from searchlet import Action, WeightedEnvironment, State


class GridAction(Action, Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class GridState(State):
    def __init__(self, loc_x: int, loc_y: int) -> None:
        self.location = (loc_x, loc_y)
    
    def __eq__(self, other):
        return self.location[0] == other.location[0] and self.location[1] == other.location[1]
    
    def __hash__(self,):
        return self.location.__hash__()

    def __str__(self,):
        return str(self.location)

    def __repr__(self, ):
        return repr(self.location)


class GridEnvironment(WeightedEnvironment):

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def initialize(self, *args, **kwargs) -> None:
        pass

    def get_actions(self, state: State) -> List[Action]:
        state = cast(GridState, state)
        actions: List[Action] = []
        if state.location[1] > 0:
            actions.append(GridAction.DOWN)
        if state.location[1] < self.height:
            actions.append(GridAction.UP)
        if state.location[0] > 0:
            actions.append(GridAction.LEFT)
        if state.location[0] < self.width:
            actions.append(GridAction.RIGHT)

        return actions

    def apply_action(self, action: Action, state: State) -> Tuple[State, Optional[Action]]:
        inv_action = None
        state = cast(GridState, state)
        x_delta = 0
        y_delta = 0
        if action is GridAction.UP:
            y_delta += 1
            inv_action = GridAction.DOWN
        elif action is GridAction.DOWN:
            y_delta -= 1
            inv_action = GridAction.UP
        elif action is GridAction.LEFT:
            x_delta -= 1
            inv_action = GridAction.RIGHT
        elif action is GridAction.RIGHT:
            x_delta += 1
            inv_action = GridAction.LEFT

        new_state = GridState(state.location[0] + x_delta, state.location[1] + y_delta)

        return (new_state, inv_action)

    def get_value(self, state: State) -> float:
        return 0

    def get_cost(self, action: Action, state: State) -> float:
        return 1
