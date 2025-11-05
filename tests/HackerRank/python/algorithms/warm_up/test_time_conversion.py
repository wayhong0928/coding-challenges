import pytest

from HackerRank.python.algorithms.warm_up.time_conversion import timeConversion


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("07:05:45PM", "19:05:45"),
        ("12:00:00AM", "00:00:00"),  # midnight
        ("12:00:00PM", "12:00:00"),  # noon
        ("01:00:00AM", "01:00:00"),
        ("11:59:59PM", "23:59:59"),
        ("04:59:59AM", "04:59:59"),
        ("12:01:00AM", "00:01:00"),
        ("12:01:00PM", "12:01:00"),
    ],
)
def test_time_conversion(inp, expected):
    """Verify timeConversion converts 12-hour clock strings to 24-hour format."""
    assert timeConversion(inp) == expected
