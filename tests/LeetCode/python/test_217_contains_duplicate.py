import pytest
from LeetCode.python._217_contains_duplicate import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),  # Example 1: Basic case with a duplicate
        ([1, 2, 3, 4], False),  # Example 2: All elements are distinct
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),  # Example 3: Multiple duplicates
        ([], False),  # Edge case: Empty list
        ([1], False),  # Edge case: Single element
        ([5, 5, 5, 5], True),  # Edge case: All elements are the same
        ([-1, 0, 1, -1], True),  # Edge case: With negative numbers
        ([0], False),  # Edge case: Single zero
    ],
)
def test_contains_duplicate(nums: list[int], expected: bool):
    """
    Test the containsDuplicate method with various inputs.
    """
    solution = Solution()
    assert solution.containsDuplicate(nums) == expected
