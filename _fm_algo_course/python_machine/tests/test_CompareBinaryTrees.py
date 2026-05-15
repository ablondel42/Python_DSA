import pytest
from src.day1.CompareBinaryTrees import compare_binary_trees, BinaryNode


def test_compare_binary_trees():
    a = BinaryNode(7)
    a.right = BinaryNode(15)
    a.right.left = BinaryNode(10)
    a.right.right = BinaryNode(20)
    a.left = BinaryNode(5)
    a.left.left = BinaryNode(2)
    a.left.right = BinaryNode(5)

    b = BinaryNode(7)
    b.right = BinaryNode(15)
    b.right.left = BinaryNode(10)
    b.right.right = BinaryNode(20)
    b.left = BinaryNode(5)
    b.left.left = BinaryNode(2)
    b.left.right = BinaryNode(5)

    c = BinaryNode(7)
    c.right = BinaryNode(15)
    c.right.left = BinaryNode(10)
    c.right.right = BinaryNode(20)
    c.left = BinaryNode(5)
    c.left.left = BinaryNode(2)

    assert compare_binary_trees(a, b) is True
    assert compare_binary_trees(a, c) is False
