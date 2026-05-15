import pytest
from src.day1.DFSGraphList import dfs_graph_list


def test_dfs_graph_list():
    graph = [
        [1, 3],
        [0],
        [1, 4],
        [0],
        [2],
    ]

    assert dfs_graph_list(graph, 0, 4) is True
    assert dfs_graph_list(graph, 0, 5) is False
