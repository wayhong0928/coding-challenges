#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# 用迴圈逐一檢查 set 當中有沒有重複的資料，如果有就回傳，如果沒有就新增該筆資料。

from typing import List


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False


# @lc code=end
