# Next node in binary tree

## Question
> Given a binary tree and one node, please find the next node in the ```inorder``` traversal.

### Solution
We'll use recursion again so the time complexity is <em>O</em>(<em>n</em>). The space complexity is <em>O</em>(<em>n</em>) too since we created extra variables to save the output inorder traversal list.
```python
from collections import deque


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
        if inorder.index(node) == len(inorder)-1:
            print("There is no next node.")
        else:
            node_next = inorder[inorder.index(node)+1]
            return node_next
```