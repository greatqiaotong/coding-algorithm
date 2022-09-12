from tests.conftest import *
from typing import Optional

class Solution:
    def reverse_linked_list_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    def reverse_linked_list_recursive(self, head: Optional[ListNode], prev: Optional[ListNode]=None) -> Optional[ListNode]:
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverse_linked_list_recursive(next, head)
