import pytest
from src.day1.SinglyLinkedList import SinglyLinkedList
from tests.test_ArrayList import assert_list_helper


def test_singly_linked_list():
    linked_list = SinglyLinkedList()
    assert_list_helper(linked_list)
