import pytest
from src.day1.LRU import LRU


def test_lru():
    lru = LRU(3)

    lru.update("foo", 5)
    assert lru.get("foo") == 5

    lru.update("bar", 10)
    lru.update("baz", 15)
    
    assert lru.get("foo") == 5
    assert lru.get("bar") == 10
    assert lru.get("baz") == 15

    # Adding a 4th item should evict the least recently used
    lru.update("qux", 20)
    
    # "foo" or "bar" should be evicted (whichever is least recently used)
    assert lru.get("qux") == 20
