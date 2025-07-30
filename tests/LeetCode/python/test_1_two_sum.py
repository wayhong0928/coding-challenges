from LeetCode.python._1_two_sum import Solution


def test_case_1():
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) in ([0, 1], [1, 0])


def test_case_2():
    sol = Solution()
    assert sol.twoSum([3, 2, 4], 6) in ([1, 2], [2, 1])


def test_no_solution():
    sol = Solution()
    assert sol.twoSum([1, 2, 3], 7) == []
