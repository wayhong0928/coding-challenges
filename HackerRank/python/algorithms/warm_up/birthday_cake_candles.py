#
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    tallest = max(candles)
    return candles.count(tallest)
