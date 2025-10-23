# 0070_climbing_stairs/test_solution.py

import pytest

from .solution import climb_stairs

# Test cases are tuples of (input_n, expected_output)
test_cases = [
    # Problem examples
    (2, 2),
    (3, 3),
    # Base cases
    (1, 1),
    # Further test cases
    (4, 5),
    (5, 8),
    (6, 13),
    # A larger number to test for efficiency and handling of the Fibonacci sequence
    (10, 89),
    # Test constraint boundaries
    (45, 1836311903),
]


@pytest.mark.parametrize("n, expected", test_cases)
def test_climb_stairs(n, expected):
    """
    Tests the climb_stairs function with various inputs.
    """
    assert climb_stairs(n) == expected


def test_climb_stairs_constraint_min():
    """
    Tests the minimum constraint for n.
    """
    assert climb_stairs(1) == 1
