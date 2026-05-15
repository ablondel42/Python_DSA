import pytest
from src.day1.BTInOrder import in_order_search, BinaryNode


def test_in_order_search():
    head = BinaryNode(7)
    head.right = BinaryNode(15)
    head.right.left = BinaryNode(10)
    head.right.right = BinaryNode(20)
    head.left = BinaryNode(5)
    head.left.left = BinaryNode(2)
    head.left.right = BinaryNode(5)

    result = in_order_search(head)
    assert result == [2, 5, 5, 7, 10, 15, 20]
