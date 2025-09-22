import pytest

from HackerRank.python.algorithms.warm_up.birthday_cake_candles import (
    birthdayCakeCandles,
)


@pytest.mark.parametrize(
    "candles, expected",
    [
        ([3, 2, 1, 3], 2),
        ([4, 4, 1, 3], 2),
    ],
)
def test_birthday_cake_candles(candles, expected):
    assert birthdayCakeCandles(candles) == expected
