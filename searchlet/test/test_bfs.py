# Copyright (c) 2018 David Chan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pytest

from searchlet.environments import GridEnvironment, GridState
from searchlet.algorithms import BFS


def test_bfs():
    # First create and initialize the environment
    env = GridEnvironment(10, 10)
    env.initialize()

    # Get the start and goal
    start = GridState(0, 0)
    goal = GridState(5, 5)

    # Solve the problem
    path = BFS.solve(env, start, goal)

    if path[0] is None:
        raise AssertionError("BFS could not find feasible path in solvable environment")


if __name__ == '__main__':
    pytest.main()