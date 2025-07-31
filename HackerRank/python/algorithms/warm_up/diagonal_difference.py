#!/bin/python3
# https://www.hackerrank.com/challenges/diagonal-difference/problem
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

# 主要的對角線是 arr[i][i]，從左上到右下
# 副對角線是 arr[i][len(arr) - i - 1]，從右上到左下
# 各自相加之後回傳絕對值


def diagonalDifference(arr):
    left = 0
    right = 0
    for i in range(0, len(arr)):
        left += arr[i][i]
        right += arr[i][len(arr) - i - 1]
    return abs(left - right)
