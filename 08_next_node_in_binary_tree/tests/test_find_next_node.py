from find_next_node import TreeNode, Solution
from typing import Optional


def to_binary_tree(items: list[int]) -> Optional[TreeNode]:
    """Create binary tree from list of values in bfs order.
    :param list[int] items: list of values
    :return Optional[TreeNode]: returned binary tree
    """    
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        # if n <= index or items[index] is None:
        if n <= index or items[index] is None:
            return

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


def test_node_with_right_subtree():
    bfs = [1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None]
    tree = to_binary_tree(bfs)
    node = 2
    solution = Solution()
    assert solution.find_next_node(tree, node) == 8


def test_node_with_no_right_subtree():
    bfs = [1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None]
    tree = to_binary_tree(bfs)
    node = 4
    solution = Solution()
    assert solution.find_next_node(tree, node) == 2


def test_node_with_no_next_node(capfd):
    bfs = [1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None]
    tree = to_binary_tree(bfs)
    node = 7
    solution = Solution()
    result = solution.find_next_node(tree, node)
    out, err = capfd.readouterr()
    assert out == "There is no next node.\n"


def test_tree_with_only_left_node():
    bfs = [1, 2, None, 3, None, None, None]
    tree = to_binary_tree(bfs)
    node = 2
    solution = Solution()
    assert solution.find_next_node(tree, node) == 1


def test_tree_with_only_right_node():
    bfs = [1, None, 2, None, None, None, 3]
    tree = to_binary_tree(bfs)
    node = 2
    solution = Solution()
    assert solution.find_next_node(tree, node) == 3

def test_tree_with_one_node(capfd):
    bfs = [1, None, None]
    tree = to_binary_tree(bfs)
    node = 1
    solution = Solution()
    result = solution.find_next_node(tree, node)
    out, err = capfd.readouterr()
    assert out == "There is no next node.\n"