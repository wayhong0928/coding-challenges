import sys
from io import StringIO

from HackerRank.python.algorithms.warm_up.mini_max_sum import miniMaxSum


def _capture_output(arr):
    buf = StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        miniMaxSum(arr)
    finally:
        sys.stdout = old
    return buf.getvalue()


def test_sample():
    out = _capture_output([1, 2, 3, 4, 5])
    assert out == "10 14\n"


def test_all_large_values():
    arr = [10**9, 10**9, 10**9, 10**9, 10**9]
    out = _capture_output(arr)
    assert out == "4000000000 4000000000\n"
