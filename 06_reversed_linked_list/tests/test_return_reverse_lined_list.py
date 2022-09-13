from return_reverse_linked_list import Solution
from tests.conftest import *


def test_empty_linked_list_iterative(create_empty_linked_list):
    solution = Solution()
    assert (
        linked_list_to_list(
            solution.reverse_linked_list_iterative(create_empty_linked_list)
        )
        == []
    )


def test_empty_linked_list_recursive(create_empty_linked_list):
    solution = Solution()
    assert (
        linked_list_to_list(
            solution.reverse_linked_list_recursive(create_empty_linked_list)
        )
        == []
    )


def test_linked_list_with_one_item_iterative(create_linked_list_with_one_item):
    solution = Solution()
    assert linked_list_to_list(
        solution.reverse_linked_list_iterative(create_linked_list_with_one_item)
    ) == [1]


def test_linked_list_with_one_item_recursive(create_linked_list_with_one_item):
    solution = Solution()
    assert linked_list_to_list(
        solution.reverse_linked_list_recursive(create_linked_list_with_one_item)
    ) == [1]


def test_linked_list_iterative(create_linked_list):
    solution = Solution()
    assert linked_list_to_list(
        solution.reverse_linked_list_iterative(create_linked_list)
    ) == [5, 4, 3, 2, 1]


def test_linked_list_recursive(create_linked_list):
    solution = Solution()
    assert linked_list_to_list(
        solution.reverse_linked_list_recursive(create_linked_list)
    ) == [5, 4, 3, 2, 1]
