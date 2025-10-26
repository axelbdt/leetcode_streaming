import pytest
from solution import coin_change

test_cases = [
    ([1, 2, 5], 5, 4),
    ([2], 3, 0),
    ([10], 10, 1),
]


@pytest.mark.parametrize("coins, amount, expected", test_cases)
def test_solution(coins, amount, expected):
    assert coin_change(coins, amount) == expected
