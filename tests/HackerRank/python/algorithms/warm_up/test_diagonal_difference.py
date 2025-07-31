import pytest
from HackerRank.python.algorithms.warm_up.diagonal_difference import diagonalDifference


@pytest.mark.parametrize(
    "arr, expected",
    [
        # 標準範例
        ([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15),
        # 3x3 另一組
        ([[1, 2, 3], [4, 5, 6], [9, 8, 9]], 2),
        # 單一元素
        ([[7]], 0),
        ([[1]], 0),
        # 全零
        ([[0, 0], [0, 0]], 0),
        # 偶數階
        ([[1, 2], [3, 4]], 0),
        # 奇數階
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0),
        # 大數
        ([[1000000, 2, 3], [4, 5000000, 6], [7, 8, 9000000]], 9999990),
        # 只有主對角線有值
        ([[5, 0, 0], [0, 5, 0], [0, 0, 5]], 10),
        # 只有副對角線有值
        ([[0, 0, 5], [0, 5, 0], [5, 0, 0]], 10),
        # 全負數
        ([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]], 0),
        # 混合正負，主副對角都 15
        ([[1, -2, 3], [-4, 5, -6], [7, -8, 9]], 0),
    ],
)
def test_diagonal_difference(arr, expected):
    assert diagonalDifference(arr) == expected


def test_diagonal_difference_extreme():
    # 最大最小值
    import sys

    maxv, minv = sys.maxsize, -sys.maxsize - 1
    arr = [[maxv, 0, minv], [0, 0, 0], [minv, 0, maxv]]
    assert diagonalDifference(arr) == abs((maxv + 0 + maxv) - (minv + 0 + minv))
