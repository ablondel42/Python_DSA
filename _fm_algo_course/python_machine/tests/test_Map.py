import pytest
from src.day1.Map import Map


def test_map():
    my_map = Map()

    my_map.set("foo", 5)
    assert my_map.get("foo") == 5
    assert my_map.has("foo") is True

    my_map.set("bar", 10)
    assert my_map.get("bar") == 10
    assert my_map.has("bar") is True

    my_map.delete("foo")
    assert my_map.get("foo") is None
    assert my_map.has("foo") is False
