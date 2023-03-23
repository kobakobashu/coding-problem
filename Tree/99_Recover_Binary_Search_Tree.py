"""
You are given the root of a binary search tree (BST), 
where the values of exactly two nodes of the tree 
were swapped by mistake. Recover the tree without changing its structure.
"""
from typing import Optional, List

class TreeNode:
    def __init__(
        self,
        val: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class BSTRecover:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        arr = self.inorder_traversal(root)
        sorted_num = sorted([node.val for node in arr])
        for i in range(len(arr)):
            arr[i].val = sorted_num[i]
        return root
    
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[TreeNode]:
        if not root:
            return []

        return self.inorder_traversal(root.left) + [root] + self.inorder_traversal(root.right)
