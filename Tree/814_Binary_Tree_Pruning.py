from typing import Optional


class TreeNode:
    def __init__(
            self, 
            val: int = 0,
            left: Optional["TreeNode"] = None,
            right: Optional["TreeNode"] = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(
            self,
            root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if not root.left and not root.right and root.val == 0:
            return None
        
        return root
