import pytest
from src.day1.TwoCrystalBalls import two_crystal_balls


def test_two_crystal_balls():
    breaks = [False, False, False, False, False, True, True, True]
    assert two_crystal_balls(breaks) == 5

    breaks = [True] * 100
    assert two_crystal_balls(breaks) == 0

    breaks = [False] * 100
    assert two_crystal_balls(breaks) == -1
