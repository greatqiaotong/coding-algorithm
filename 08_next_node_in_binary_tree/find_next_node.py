from typing import Optional, Union
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def inorder_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret


class Solution:
    def find_next_node(self, tree: Optional[TreeNode], node: int) -> Union[None, int]:
        t = Tree()
        t.root = tree
        inorder = t.inorder_traversal()
        if inorder.index(node) == len(inorder) - 1:
            print("There is no next node.")
        else:
            node_next = inorder[inorder.index(node) + 1]
            return node_next
