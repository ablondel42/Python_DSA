import pytest
from src.day1.LinearSearchList import linear_search


def test_linear_search():
    arr = [1, 3, 4, 6, 8, 9, 11]
    assert linear_search(arr, 8) is True
    assert linear_search(arr, 5) is False
