import pytest
from typing import List
import sys
from pathlib import Path

# This is needed so that the local LeetCode package can be found
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from LeetCode.python._49_group_anagrams import Solution


def _normalize(groups: List[List[str]]) -> set[tuple[str, ...]]:
    """Normalize list of groups for unordered comparison.
    - Sort each inner group (strings order doesn't matter)
    - Use a set of tuples so group order doesn't matter
    """
    return {tuple(sorted(g)) for g in groups}


Solution = Solution


@pytest.mark.parametrize(
    "strs, expected",
    [
        # Example 1
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        # Example 2
        ([""], [[""]]),
        # Example 3
        (["a"], [["a"]]),
        # Additional: multiple groups and singletons
        (
            ["ab", "ba", "abc", "cab", "bca", "abcd"],
            [["ab", "ba"], ["abc", "cab", "bca"], ["abcd"]],
        ),
        # Duplicates of the same string
        (["a", "a", "a"], [["a", "a", "a"]]),
        # Empty strings duplicates
        (["", ""], [["", ""]]),
        # Mixed real-world words
        (
            [
                "listen",
                "silent",
                "enlist",
                "inlets",
                "google",
                "gogole",
                "abc",
            ],
            [["listen", "silent", "enlist", "inlets"], ["google", "gogole"], ["abc"]],
        ),
    ],
)
def test_group_anagrams(strs: List[str], expected: List[List[str]]):
    sol = Solution()
    result = sol.groupAnagrams(strs)
    assert _normalize(result) == _normalize(expected)
