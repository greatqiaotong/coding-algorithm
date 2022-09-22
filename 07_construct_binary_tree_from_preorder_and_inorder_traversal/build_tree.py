from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_binary_tree(items: list[int]) -> Optional[TreeNode]:
    """Create binary tree from list of values.
    :param list[int] items: list of values
    :return Optional[TreeNode]: returned binary tree
    """
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


class Solution:
    def build_tree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """Build the binary tree from given preorder and inorder traversal.

        :param list[int] preorder: preorder traversal in a list
        :param list[int] inorder: inorder traversal in a list
        :return Optional[TreeNode]: binary tree
        """
        if not preorder or not inorder:
            return None
        index = inorder.index(preorder[0])
        left = inorder[:index]
        right = inorder[index + 1 :]
        root = TreeNode(preorder[0])
        root.left = self.build_tree(preorder[1 : 1 + len(left)], left)
        root.right = self.build_tree(preorder[-len(right) :], right)
        return root
