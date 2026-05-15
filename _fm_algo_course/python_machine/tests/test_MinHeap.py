import pytest
from src.day1.MinHeap import MinHeap


def test_min_heap():
    heap = MinHeap()

    heap.insert(5)
    heap.insert(3)
    heap.insert(69)
    heap.insert(420)
    heap.insert(4)
    heap.insert(1)
    heap.insert(8)
    heap.insert(7)

    assert heap.delete() == 1
    assert heap.delete() == 3
    assert heap.delete() == 4
    assert heap.delete() == 5
    assert heap.delete() == 7
    assert heap.delete() == 8
    assert heap.delete() == 69
    assert heap.delete() == 420
