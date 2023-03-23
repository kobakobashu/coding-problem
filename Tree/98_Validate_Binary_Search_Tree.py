from collections import deque
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


class ValidBST:
    def is_valid_BST(self, root: Optional[TreeNode]) -> bool:
        inorder = self.inorder_list(root)
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i - 1]:
                return False
        
        return True
    
    def inorder_list(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        inorder = []
        stack = deque()
        while stack or node:
            if node:
                stack.append(node)
                node = node.left

            else:
                node = stack.pop()
                inorder.append(node.val)
                node = node.right
        
        return inorder

    """
    def is_valid_BST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            raise ValueError("invalid input")
        
        cur = root
        stack = deque()
        stack.append([root, None, None])
        while stack:
            cur, left, right = stack.pop()
            if not cur:
                continue

            if left is not None and left >= cur.val:
                return False

            if right is not None and right <= cur.val:
                return False

            stack.append([cur.left, left, cur.val])
            stack.append([cur.right, cur.val, right])
        
        return True
    """


if __name__ == "__main__" :
    ans = ValidBST().is_valid_BST(TreeNode(0, None, TreeNode(-1)))
    print(ans)