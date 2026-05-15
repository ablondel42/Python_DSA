import pytest
from src.day1.Trie import Trie


def test_trie():
    trie = Trie()

    trie.insert("hello")
    assert trie.find("hello") is True
    assert trie.find("hell") is True
    assert trie.find("hello world") is False

    trie.delete("hello")
    assert trie.find("hello") is False
    assert trie.find("hell") is False
