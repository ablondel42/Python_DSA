import pytest
from src.day1.BFSGraphMatrix import bfs_graph_matrix


def test_bfs_graph_matrix():
    graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
    ]

    assert bfs_graph_matrix(graph, 0, 4) is True
    assert bfs_graph_matrix(graph, 0, 5) is False
