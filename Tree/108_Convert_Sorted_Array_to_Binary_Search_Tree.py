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


class BSTMaker:
    def sorted_array_to_BST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sorted_array_to_BST(nums[:mid])
        node.right = self.sorted_array_to_BST(nums[mid + 1:])
        return node


if __name__ == "__main__":
    print(BSTMaker().sorted_array_to_BST([1,2,3]).val)