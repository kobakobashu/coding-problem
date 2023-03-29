from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTNodeRemover:
    def delete_node(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < key:
            root.right = self.delete_node(root.right, key)
        
        elif root.val > key:
            root.left = self.delete_node(root.left, key)
        
        else:
            if not root.left:
                return root.right

            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            
            root.val = tmp.val
            root.left = self.delete_node(root.left, tmp.val)
        
        return root