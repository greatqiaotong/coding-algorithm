import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(arr):
    if len(arr) < 1:
        return None
    elif len(arr) == 1:
        return ListNode(arr[0])
    else:
        return ListNode(arr[0], next=list_to_linked_list(arr[1:]))


@pytest.fixture()
def create_empty_linked_list():
    return list_to_linked_list([])


@pytest.fixture()
def create_linked_list_with_one_item():
    return list_to_linked_list([1])


@pytest.fixture()
def create_linked_list():
    return list_to_linked_list([1, 2, 3, 4, 5])
