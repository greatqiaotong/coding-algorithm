# Construct binary tree from preorder and inorder traversal

## Question
> Given two interger arrays ```preorder``` and ```inorder``` where ```preorder``` is the preorder traversal of a binary tree and ```inorder``` is the inorder traversal of the same tree, contruct and return the binary tree.

### Solution
Preoder traversal's first element is the tree's root, which can be used to split the tree into 2 subtrees in the inorder traversal. And then recursion is applied on subtrees. Build the tree takes <em>O</em>(<em>n</em>) in time and the space complexity is <em>O</em>(<em>n</em>) too as there are <em>n</em> nodes in the tree.
```python
class Solution:
    def build_tree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:       
        if not preorder or not inorder:
            return None
        index = inorder.index(preorder[0])
        left = inorder[:index]
        right = inorder[index + 1 :]
        root = TreeNode(preorder[0])
        root.left = self.build_tree(preorder[1 : 1 + len(left)], left)
        root.right = self.build_tree(preorder[-len(right) :], right)
        return root
```