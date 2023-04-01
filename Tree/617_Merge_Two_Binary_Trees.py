from typing import Optional


class TreeNode:
    def __init__(
        self, 
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class TreeMerger:
    def merge_trees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        
        if not root2:
            return root1
        
        root1.val = root1.val + root2.val
        root1.left = self.merge_trees(root1.left, root2.left)
        root1.right = self.merge_trees(root1.right, root2.right)

        return root1
        

if __name__ == "__main__":
    print(TreeMerger().merge_trees(TreeNode(3, TreeNode(2)), TreeNode(3, None, TreeNode(2))).val)