# Reversed linked list

## Question 1 - 剑指offer
> Given the head of a singly linked list, reverse the list, and print out the value at each node.

### Solution 1
Use stack to realise because stack is "last in, first out". Time complexity is <em>O</em>(<em>n</em>) and space complexity is <em>O</em>(<em>n</em>) since a stack needs to be created.
```python
class Solution:
    def reverse_linked_list_iterative(self, head: Optional[ListNode]) -> None:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        while stack:
            print(stack.pop())
```

### Solution 2
Recursion is kind of a stack type of structure therefore we can also use a recursive function to realise it. Time complexity is <em>O</em>(<em>n</em>) and space complexity is <em>O</em>(1).
```python
class Solution:
    def reverse_linked_list_recursive(self, head: Optional[ListNode]) -> None:
        if head:
            self.reverse_linked_list_recursive(head.next)
            print(head.val)
```

## Question 2 - [LeetCode 206](https://leetcode.com/problems/reverse-linked-list/)
> Given the head of a singly linked list, reverse the list, and return the reversed list.