import pytest
from src.day1.BTBFS import bfs_binary_tree, BinaryNode


def test_bfs_binary_tree():
    head = BinaryNode(7)
    head.right = BinaryNode(15)
    head.right.left = BinaryNode(10)
    head.right.right = BinaryNode(20)
    head.left = BinaryNode(5)
    head.left.left = BinaryNode(2)
    head.left.right = BinaryNode(5)

    result = bfs_binary_tree(head)
    assert result == [7, 5, 15, 2, 5, 10, 20]
