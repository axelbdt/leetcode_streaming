import pytest

test_cases = [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0),
]

from solution import longest_common_subsequence


@pytest.mark.parametrize("s1, s2, expected", test_cases)
def test_solution(s1, s2, expected):
    assert longest_common_subsequence(s1, s2) == expected
