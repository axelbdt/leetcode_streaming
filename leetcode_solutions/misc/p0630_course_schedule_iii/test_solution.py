import pytest
from solution import schedule_course

test_cases = [
    ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3),
    ([[1, 2]], 1),
    ([[3, 2], [4, 3]], 0),
    ([[5, 5], [4, 6], [2, 6]], 2),
]


@pytest.mark.parametrize("args,expected", test_cases)
def test_solution(args, expected):
    assert schedule_course(args) == expected
