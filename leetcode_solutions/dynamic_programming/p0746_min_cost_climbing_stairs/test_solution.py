import pytest

# Ensure the import path matches your new directory structure
from .solution import min_cost_climbing_stairs

# A list of tuples: (input_cost_array, expected_minimum_cost)
test_cases = [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ([2, 5], 2),
    ([10, 3], 3),
    ([5, 5, 5, 5, 5], 10),
    ([0, 2, 2, 1], 2),
    ([1, 5, 2, 6, 3], 6),
    ([1, 5, 2, 6, 3], 6),
]


@pytest.mark.parametrize("cost, expected", test_cases)
def test_min_cost_climbing_stairs(cost, expected):
    """
    Tests the min_cost_climbing_stairs function with various cost arrays.
    """
    assert min_cost_climbing_stairs(cost) == expected


if __name__ == "__main__":
    for cost, expected in test_cases:
        print("(" + str(cost) + ", " + str(min_cost_climbing_stairs(cost)) + "),")
