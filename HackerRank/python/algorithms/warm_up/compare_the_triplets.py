#
# https://www.hackerrank.com/challenges/compare-the-triplets/problem
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b


def compareTriplets(a, b):
    pointA = 0
    pointB = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            pointA += 1
        elif a[i] < b[i]:
            pointB += 1

    return pointA, pointB
