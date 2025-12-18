#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# 先對輸入的字串內容作排序，排序後再把一樣的字串加到同一個字典裡。

from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for str in strs:
            str_sorted = tuple(sorted(str))
            str_dict[str_sorted].append(str)

        return list(str_dict.values())


# @lc code=end
