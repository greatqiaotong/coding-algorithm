from build_tree import TreeNode
from build_tree import Solution
from typing import Optional


def tree_to_list(tree: Optional[TreeNode]) -> list[int]:
    """Convert the binary tree to a list of values.

    :param Optional[TreeNode] tree: the binary tree
    :return list[int]: returned list of values
    """
    items = []
    queue = [tree]

    while queue:
        copy = queue[:]
        queue = []

        for item in copy:
            if item is None:
                items.append(None)
                queue.append(None)
                queue.append(None)
            else:
                items.append(item.val)
                queue.append(item.left)
                queue.append(item.right)

        if all((x is None for x in queue)):
            break

    return items


def test_build_tree_empty_binary_tree():
    preorder = []
    inorder = []
    solution = Solution()
    result = solution.build_tree(preorder, inorder)
    assert result == None


def test_build_tree_symmetric_binary_tree():
    preorder = [10, 6, 4, 8, 14, 12, 16]
    inorder = [4, 6, 8, 10, 12, 14, 16]
    solution = Solution()
    result = solution.build_tree(preorder, inorder)
    assert tree_to_list(result) == [10, 6, 14, 4, 8, 12, 16]


def test_build_tree_insymmetric_binary_tree():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    result = solution.build_tree(preorder, inorder)
    assert tree_to_list(result) == [3, 9, 20, None, None, 15, 7]


def test_build_tree_only_left_node():
    preorder = [1, 2, 3, 4]
    inorder = [4, 3, 2, 1]
    solution = Solution()
    result = solution.build_tree(preorder, inorder)
    assert tree_to_list(result) == [
        1,
        2,
        None,
        3,
        None,
        None,
        None,
        4,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]


def test_build_tree_only_right_node():
    preorder = [1, 2, 3, 4]
    inorder = [1, 2, 3, 4]
    solution = Solution()
    result = solution.build_tree(preorder, inorder)
    assert tree_to_list(result) == [
        1,
        None,
        2,
        None,
        None,
        None,
        3,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        4,
    ]


def test_build_tree_one_node():
    preorder = [1]
    inorder = [1]
    solution = Solution()
    result = solution.build_tree(preorder, inorder)
    assert tree_to_list(result) == [1]
