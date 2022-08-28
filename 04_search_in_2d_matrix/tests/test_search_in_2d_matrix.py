import pytest
from search_in_2d_matrix import *


@pytest.fixture
def matrix():
    return [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]


def test_empty_matrix():
    with pytest.raises(ValueError):
        search_matrix([], 5)


def test_search_matrix_target_in(matrix):
    assert search_matrix(matrix, 5) == True


def test_search_matrix_target_in_max(matrix):
    assert search_matrix(matrix, 30) == True


def test_search_matrix_target_in_min(matrix):
    assert search_matrix(matrix, 1) == True


def test_search_matrix_target_not_in(matrix):
    assert search_matrix(matrix, 20) == False


def test_search_matrix_target_not_in_greater_than_max(matrix):
    assert search_matrix(matrix, 31) == False


def test_search_matrix_target_not_in_smaller_than_min(matrix):
    assert search_matrix(matrix, 0) == False
