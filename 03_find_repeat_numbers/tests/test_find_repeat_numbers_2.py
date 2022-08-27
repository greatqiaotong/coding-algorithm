import pytest
from find_repeat_numbers_2 import *


def test_repeat_number():
    assert find_repeat_number([2, 3, 5, 4, 3, 2, 6, 7]) == 3


def test_invalid_array():
    with pytest.raises(ValueError):
        find_repeat_number([1, 2, 3])
        find_repeat_number([-1, -1, 2])


def test_empty_array():
    with pytest.raises(ValueError):
        find_repeat_number([])
