import pytest

from . import GraphNode

test_cases = [[[1, 1, 2], [2], [3, 3], [4, 0]]]


@pytest.mark.parametrize("graph", test_cases)
def test_graph(graph):
    assert GraphNode.of(graph).__repr__() == f"GraphNode.of({graph})"
