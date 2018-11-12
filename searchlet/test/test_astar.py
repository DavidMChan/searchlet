# Copyright (c) 2018 David Chan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pytest
import math

from searchlet.environments import GridEnvironment, GridState
from searchlet.algorithms import AStar, Dijkstra, IDAStar


def test_astar_no_heuristic():
    # First create and initialize the environment
    env = GridEnvironment(10, 10)
    env.initialize()

    # Get the start and goal
    start = GridState(0, 0)
    goal = GridState(5, 5)

    # Solve the problem
    path = AStar.solve(env, start, goal)

    if path[0] is None:
        raise AssertionError("BFS could not find feasible path in solvable environment")


def test_astar_heuristic():
    # First create and initialize the environment
    env = GridEnvironment(10, 10)
    env.initialize()

    # Get the start and goal
    start = GridState(0, 0)
    goal = GridState(5, 5)

    def h_fn(x: GridState, y: GridState):
        return 1000 * math.sqrt((x.location[0] - y.location[0]) ** 2 + (x.location[1] - y.location[1]) ** 2)

    # Solve the problem
    path = AStar.solve(env, start, goal, heuristic=h_fn)

    if path[0] is None:
        raise AssertionError("BFS could not find feasible path in solvable environment")


def test_dijkstra():
    # First create and initialize the environment
    env = GridEnvironment(10, 10)
    env.initialize()

    # Get the start and goal
    start = GridState(0, 0)
    goal = GridState(5, 5)

    # Solve the problem
    path = Dijkstra.solve(env, start, goal)

    if path[0] is None:
        raise AssertionError("BFS could not find feasible path in solvable environment")

def test_idastar_heuristic():
    # First create and initialize the environment
    env = GridEnvironment(10, 10)
    env.initialize()

    # Get the start and goal
    start = GridState(0, 0)
    goal = GridState(5, 5)

    def h_fn(x: GridState, y: GridState):
        return 1000 * math.sqrt((x.location[0] - y.location[0]) ** 2 + (x.location[1] - y.location[1]) ** 2)

    # Solve the problem
    path = IDAStar.solve(env, start, goal, heuristic=h_fn)

    if path[0] is None:
        raise AssertionError("BFS could not find feasible path in solvable environment")


def test_idastar_no_heuristic():
    # First create and initialize the environment
    env = GridEnvironment(10, 10)
    env.initialize()

    # Get the start and goal
    start = GridState(0, 0)
    goal = GridState(5, 5)

    # Solve the problem
    path = IDAStar.solve(env, start, goal)

    if path[0] is None:
        raise AssertionError("BFS could not find feasible path in solvable environment")

if __name__ == '__main__':
    pytest.main()


if __name__ == '__main__':
    pytest.main()