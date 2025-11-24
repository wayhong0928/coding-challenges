import pytest

from HackerRank.python.algorithms.warm_up.compare_the_triplets import compareTriplets


@pytest.mark.parametrize(
    "a, b, expected",
    [
        # Example from problem description
        ([1, 2, 3], [3, 2, 1], (1, 1)),
        # Alice wins all categories
        ([5, 6, 7], [1, 2, 3], (3, 0)),
        # Bob wins all categories
        ([1, 2, 3], [5, 6, 7], (0, 3)),
        # All equal (no points)
        ([5, 5, 5], [5, 5, 5], (0, 0)),
        # Mixed scenarios
        ([10, 20, 30], [5, 25, 35], (1, 2)),
        ([100, 1, 50], [1, 100, 50], (1, 1)),
        # Edge cases with constraint boundaries (1-100)
        ([1, 1, 1], [100, 100, 100], (0, 3)),
        ([100, 100, 100], [1, 1, 1], (3, 0)),
        ([50, 75, 25], [50, 25, 75], (1, 1)),
        # Single point differences
        ([50, 50, 50], [49, 51, 50], (1, 1)),
    ],
)
def test_compare_triplets(a, b, expected):
    """Test compareTriplets function with various input combinations."""
    result = compareTriplets(a, b)
    assert result == expected


def test_compare_triplets_return_type():
    """Verify that the function returns a tuple of two integers."""
    result = compareTriplets([1, 2, 3], [3, 2, 1])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(score, int) for score in result)


def test_compare_triplets_scores_range():
    """Verify that scores are always between 0 and 3."""
    test_cases = [
        ([1, 2, 3], [3, 2, 1]),
        ([100, 100, 100], [1, 1, 1]),
        ([50, 50, 50], [50, 50, 50]),
    ]

    for a, b in test_cases:
        alice_score, bob_score = compareTriplets(a, b)
        assert 0 <= alice_score <= 3
        assert 0 <= bob_score <= 3
        assert alice_score + bob_score <= 3  # Can't exceed total categories
