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


class LongestPath:
    def path_finder(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.ans = 0
        self.max_unival_recursively(root)
        return self.ans
    
    def max_unival_recursively(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = self.max_unival_recursively(node.left)
        right = self.max_unival_recursively(node.right)
        left_arrow = right_arrow = 0
        if node.left and node.left.val == node.val:
            left_arrow = left + 1
        if node.right and node.right.val == node.val:
            right_arrow = right + 1
        self.ans = max(self.ans, left_arrow + right_arrow)
        return max(left_arrow, right_arrow)