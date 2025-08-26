# https://www.hackerrank.com/challenges/mini-max-sum/problem
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# 用一個迴圈把所有數值加總，同時記錄最大值/最小值，最後用加總值扣掉即可輸出。


def miniMaxSum(arr):
    minNum = arr[0]
    maxNum = 0
    total = 0
    for i in range(0, len(arr)):
        if minNum > arr[i]:
            minNum = arr[i]
        if maxNum < arr[i]:
            maxNum = arr[i]
        total += arr[i]
    print(total - maxNum, total - minNum)
