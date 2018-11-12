# Copyright (c) 2018 David Chan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pytest

from searchlet.environments import GridEnvironment, GridState
from searchlet.algorithms import DFS, DepthLimitedDFS


def test_dfs():
    # First create and initialize the environment
    env = GridEnvironment(10, 10)
    env.initialize()

    # Get the start and goal
    start = GridState(0, 0)
    goal = GridState(5, 5)

    # Solve the problem
    path = DFS.solve(env, start, goal)

    if path[0] is None:
        raise AssertionError("DFS could not find feasible path in solvable environment")


@pytest.mark.parametrize("depth", list(range(20)))
def test_depth_limited_dfs(depth):

    # First create and initialize the environment
    env = GridEnvironment(10, 10)
    env.initialize()

    # Get the start and goal
    start = GridState(0, 0)
    goal = GridState(5, 5)

    # Solve the problem
    path = DepthLimitedDFS.solve(env, start, goal, depth_limit=depth)
    if depth < 11 and path[0] is not None:
        raise AssertionError(f"Depth-Limited DFS went too deep: Depth {depth}!")
    elif depth >= 11 and path[0] is None:
        raise AssertionError(f"DFS could not find feasible path in solvable environment. Depth {depth}")


if __name__ == '__main__':
    pytest.main()