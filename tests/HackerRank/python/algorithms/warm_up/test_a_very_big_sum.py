from HackerRank.python.algorithms.warm_up.a_very_big_sum import aVeryBigSum
import pytest


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1000000001, 1000000002, 1000000003], 3000000006),  # 題目 Sample
        ([], 0),  # 空陣列
        ([42], 42),  # 單元素
    ],
)
def test_sum(nums, expected):
    assert aVeryBigSum(nums) == expected
