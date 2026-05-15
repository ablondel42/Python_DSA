import pytest
from src.day1.ArrayList import ArrayList


def assert_list_helper(list_obj):
    """Helper function to test list implementations."""
    list_obj.append(5)
    list_obj.append(7)
    list_obj.append(9)

    assert list_obj.get(2) == 9
    assert list_obj.removeAt(1) == 7
    assert list_obj.length == 2

    list_obj.append(11)
    assert list_obj.removeAt(1) == 9
    assert list_obj.remove(9) is None
    assert list_obj.removeAt(0) == 5
    assert list_obj.removeAt(0) == 11
    assert list_obj.length == 0

    list_obj.prepend(5)
    list_obj.prepend(7)
    list_obj.prepend(9)

    assert list_obj.get(2) == 5
    assert list_obj.get(0) == 9
    assert list_obj.remove(9) == 9
    assert list_obj.length == 2
    assert list_obj.get(0) == 7


def test_array_list():
    list_obj = ArrayList(3)
    assert_list_helper(list_obj)
