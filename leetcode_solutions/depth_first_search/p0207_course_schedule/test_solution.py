import pytest

test_cases = [
    {"input": {"num_courses": 2, "prerequisites": [[1, 0]]}, "output": True},
    {"input": {"num_courses": 2, "prerequisites": [[0, 1]]}, "output": True},
    {"input": {"num_courses": 2, "prerequisites": [[1, 0], [0, 1]]}, "output": False},
    {
        "input": {"num_courses": 5, "prerequisites": [[1, 4], [2, 4], [3, 1], [3, 2]]},
        "output": True,
    },
]

from solution import can_finish


@pytest.mark.parametrize("test_case", test_cases)
def test_canFinish(test_case):
    assert can_finish(**test_case["input"]) == test_case["output"]
