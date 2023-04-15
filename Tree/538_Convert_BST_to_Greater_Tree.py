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


class Converter:
    def convert_BST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque()
        node = root
        cur_sum = 0
        while node or stack:
            if node:
                stack.append(node)
                node = node.right
            
            else:
                node = stack.pop()
                cur_sum += node.val
                node.val = cur_sum
                node = node.left
        
        return root
