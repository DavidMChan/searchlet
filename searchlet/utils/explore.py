"""Utilities for exploring envirionments
"""

import random

from searchlet import Environment, State
from typing import List

def generate_random_rollout(env: Environment, state: State, depth: int) -> List[State]:
    """Generate a random rollout from an environment given the starting state and depth
    
    :param env: The environment to use
    :type env: Environment
    :param state: The starting state of the rollout
    :type state: State
    :param depth: The depth of the rollout
    :type depth: int
    :return: The list of states in the rollout
    :rtype: List[State]
    """
    states = []
    states.append(state)
    for _ in range(depth):
        action = random.choice(env.get_actions(state))
        state = env.apply_action(action, state)[0]
        states.append(state)
 
    return states
