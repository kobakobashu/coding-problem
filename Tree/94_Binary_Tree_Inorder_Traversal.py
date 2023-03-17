# node = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(3))
# Inorder().inorder_traversal(node) -> [3, 2, 4, 1, 3]

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(
        self, 
        val: int, 
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
    

class Inorder:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """Function to traverse the root from left to right
        
        Args:
            root(Optional[TreeNode]): A root node
        
        Returns:
            List[int]: A list of integer
        """
        ans = []
        node = root
        stack = deque()
        while node or stack:
            if node:
                stack.append(node)
                node = node.left

            else:
                node = stack.pop()
                ans.append(node.val)
                node = node.right
        
        return ans


if __name__ == "__main__":
    node = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(3))
    print(Inorder().inorder_traversal(node))