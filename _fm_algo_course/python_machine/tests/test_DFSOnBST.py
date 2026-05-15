import pytest
from src.day1.DFSOnBST import dfs_on_bst, BSTNode


def test_dfs_on_bst():
    head = BSTNode(7)
    head.right = BSTNode(15)
    head.right.left = BSTNode(10)
    head.right.right = BSTNode(20)
    head.left = BSTNode(5)
    head.left.left = BSTNode(2)
    head.left.right = BSTNode(5)

    assert dfs_on_bst(head, 15) is True
    assert dfs_on_bst(head, 100) is False
    assert dfs_on_bst(head, 5) is True
