import pytest
from find_repeat_numbers_1 import *


def test_single_repeat_number():
    assert find_repeat_number([1, 2, 2, 2, 3]) == 2


def test_multiple_repeat_numbers():
    assert (
        find_repeat_number([2, 3, 1, 0, 2, 5, 3]) == 2
        or find_repeat_number([2, 3, 1, 0, 2, 5, 3]) == 3
    )


def test_invalid_array():
    with pytest.raises(ValueError):
        find_repeat_number([4, 4, 5])
        find_repeat_number([-1, -1, 2])


def test_empty_array():
    with pytest.raises(ValueError):
        find_repeat_number([])
