from tests.conftest import *
from typing import Optional


class Solution:
    def reverse_linked_list_iterative(self, head: Optional[ListNode]) -> None:
        """Print node value in reverse order for a linked list using stack.

        :param Optional[ListNode] head: linked list
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        while stack:
            print(stack.pop())

    def reverse_linked_list_recursive(self, head: Optional[ListNode]) -> None:
        """Print node value in reverse order for a linked list using recursive function.

        :param Optional[ListNode] head: linked list
        """
        if head:
            self.reverse_linked_list_recursive(head.next)
            print(head.val)
