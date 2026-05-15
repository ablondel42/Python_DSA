import pytest
from src.day1.DoublyLinkedList import DoublyLinkedList
from tests.test_ArrayList import assert_list_helper


def test_doubly_linked_list():
    linked_list = DoublyLinkedList()
    assert_list_helper(linked_list)
