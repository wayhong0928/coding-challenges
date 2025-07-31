import io
import sys
import pytest
from HackerRank.python.algorithms.warm_up.plus_minus import plusMinus


def run_plus_minus(arr):
    captured = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = captured
    try:
        plusMinus(arr)
    finally:
        sys.stdout = sys_stdout
    return captured.getvalue().splitlines()


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 1, 0, -1, -1], ["0.400000", "0.400000", "0.200000"]),
        ([1, -2, -7, 9, 1, -8, -5], ["0.428571", "0.571429", "0.000000"]),
        ([0, 0, 0, 0], ["0.000000", "0.000000", "1.000000"]),
        ([1, 2, 3, 4], ["1.000000", "0.000000", "0.000000"]),
        ([-1, -2, -3, -4], ["0.000000", "1.000000", "0.000000"]),
        ([0], ["0.000000", "0.000000", "1.000000"]),
        ([1], ["1.000000", "0.000000", "0.000000"]),
        ([-1], ["0.000000", "1.000000", "0.000000"]),
    ],
)
def test_plus_minus(arr, expected):
    output = run_plus_minus(arr)
    assert output == expected
