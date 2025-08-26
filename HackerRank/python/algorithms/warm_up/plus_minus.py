#!/bin/python3
# https://www.hackerrank.com/challenges/plus-minus/problem
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# 分別計算正數、負數和零的比例，用小數點後六位輸出。


def plusMinus(arr):
    n = len(arr)
    positive = sum(1 for j in arr if j > 0)
    negative = sum(1 for j in arr if j < 0)
    zero = n - positive - negative

    print(f"{positive / n:.6f}")
    print(f"{negative / n:.6f}")
    print(f"{zero / n:.6f}")
