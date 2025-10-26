import pytest
from solution import coin_change

test_cases = [([1, 2, 5], 11, 3), ([2], 3, -1), ([1], 0, 0), ([1, 2147483647], 2, 2)]


@pytest.mark.parametrize("coins, amount, expected", test_cases)
def test_solution(coins, amount, expected):
    assert coin_change(coins, amount) == expected
