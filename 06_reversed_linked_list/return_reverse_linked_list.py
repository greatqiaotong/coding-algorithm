from tests.conftest import *
from typing import Optional


class Solution:
    def reverse_linked_list_iterative(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Return the given linked list in reverse order iteratively.

        :param Optional[ListNode] head: linked list
        :return Optional[ListNode]: reversed linked list
        """
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def reverse_linked_list_recursive(
        self, head: Optional[ListNode], prev: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        """Return the given linked list in reverse order recursively.

        :param Optional[ListNode] head: linked list
        :param Optional[ListNode] prev: the previous node in the current linked list, defaults to None
        :return Optional[ListNode]: reversed linked list
        """
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverse_linked_list_recursive(next, head)
