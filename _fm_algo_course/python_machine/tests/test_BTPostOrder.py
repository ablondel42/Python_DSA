import pytest
from src.day1.BTPostOrder import post_order_search, BinaryNode


def test_post_order_search():
    head = BinaryNode(7)
    head.right = BinaryNode(15)
    head.right.left = BinaryNode(10)
    head.right.right = BinaryNode(20)
    head.left = BinaryNode(5)
    head.left.left = BinaryNode(2)
    head.left.right = BinaryNode(5)

    result = post_order_search(head)
    assert result == [2, 5, 5, 10, 20, 15, 7]
