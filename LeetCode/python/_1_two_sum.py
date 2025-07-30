#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
# 題目：Two Sum
# 給定一個整數陣列 nums 和一個目標值 target，
# 陣列某兩個數字相加會等於 target，回傳它們的 index 位置。
# 假設每個輸入只會有一組答案，且同一元素不能重複使用。
# 使用字典來記錄已遍歷過的數字及其索引，時間複雜度為 O(n)。

from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex: Dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numToIndex:
                return [numToIndex[complement], i]
            numToIndex[num] = i
        return []


# @lc code=end
