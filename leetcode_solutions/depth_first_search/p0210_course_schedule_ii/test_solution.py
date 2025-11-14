import pytest

test_cases = [
    {"num_courses": 2, "prerequisites": [[0, 1]]},
    {
        "num_courses": 4,
        "prerequisites": [[0, 1], [2, 0], [3, 1], [3, 2]],
    },
]

from solution import find_order


@pytest.mark.parametrize("test_case", test_cases)
def test_find_order(test_case):
    order = find_order(**test_case)
    prequisites = test_case["prerequisites"]
    index = [order.index(i) for i in range(len(order))]
    assert all(index[course] > index[preq] for course, preq in prequisites)
