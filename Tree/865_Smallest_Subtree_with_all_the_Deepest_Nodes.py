from typing import Dict, Optional

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
    def subtree_with_all_deepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        subtree, _ = self.find_sub_tree(root)
        return subtree
    
    def find_sub_tree(self, root: TreeNode) -> Dict[TreeNode, int]:
        if not root:
            return [None, 0]

        left_node, left_depth = self.find_sub_tree(root.left)
        right_node, right_depth = self.find_sub_tree(root.right)

        if left_depth == right_depth:
            return [root, left_depth + 1]
        
        if left_depth > right_depth:
            return [left_node, left_depth + 1]
        
        return [right_node, right_depth + 1]
