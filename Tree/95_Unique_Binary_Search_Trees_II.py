"""
Given an integer n, return all the structurally 
unique BST's (binary search trees), which has exactly 
n nodes of unique values from 1 to n. Return the answer in any order.
"""

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


class UniqueBSTTree:
    def unique_tree_creater(self, n: int) -> List[TreeNode]:
        return self.unique_tree_creater_recursive(1, n)
    
    def unique_tree_creater_recursive(self, start: int, end: int) -> List[TreeNode]:
        if start > end:
            return [None]
        
        if start == end:
            return [TreeNode(start)]
        
        possible_tree = []
        for i in range(start, end + 1):
            left_tree = self.unique_tree_creater_recursive(start, i-1)
            right_tree = self.unique_tree_creater_recursive(i+1, end)
            for left in left_tree:
                for right in right_tree:
                    cur = TreeNode(i)
                    cur.left = left
                    cur.right = right
                    possible_tree.append(cur)
        
        return possible_tree


if __name__ == "__main__":
    maker = UniqueBSTTree()
    ans = maker.unique_tree_creater(3)
    print(ans)
    print(ans[1].right.left.val)