from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class BSTTrimer:
    def trim_BST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < low:
            return self.trim_BST(root.right, low, high)
        
        if root.val > high:
            return self.trim_BST(root.left, low, high)
        
        root.left = self.trim_BST(root.left, low, high)
        root.right = self.trim_BST(root.right, low, high)

        return root
