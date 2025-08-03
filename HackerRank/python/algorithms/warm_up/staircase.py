#!/bin/python3
# https://www.hackerrank.com/challenges/staircase/problem
#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    for i in range(0, n):
        print(" " * (n - i - 1) + "#" * (i + 1))
