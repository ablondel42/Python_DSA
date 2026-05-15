import pytest
from src.day1.BinarySearchList import binary_search


def test_binary_search():
    arr = [1, 3, 4, 6, 8, 9, 11]
    assert binary_search(arr, 8) is True
    assert binary_search(arr, 5) is False
