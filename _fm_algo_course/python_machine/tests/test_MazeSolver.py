import pytest
from src.day1.MazeSolver import maze_solver


def test_maze_solver():
    maze = [
        "xxxxxxxxxx x",
        "x x x x x x",
        "x           ",
        "x xxxxxxxxxx",
        "x          x",
        "x xxxxxxxxxx",
        "x x x x x xx",
        "x x S x E xx",
    ]

    result = maze_solver(maze, "x", (10, 7), (10, 1))

    assert result is not None
    assert len(result) > 0
    assert result[0] == (10, 7)
    assert result[-1] == (10, 1)
