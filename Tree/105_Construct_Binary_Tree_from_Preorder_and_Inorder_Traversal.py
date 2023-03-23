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


class CreateBinaryTree:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            node = TreeNode(preorder[0])
            idx = inorder.index(preorder[0])
            node.left = self.buildTree(preorder[1: 1 + idx], inorder[: idx])
            node.right = self.buildTree(preorder[1 + idx:], inorder[1 + idx:])
        
        else:
            return None
        
        return node
    

if __name__ == "__main__":
    ans = CreateBinaryTree().buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(ans.val)
