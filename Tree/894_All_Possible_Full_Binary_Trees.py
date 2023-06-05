from collections import deque
from typing import Optional, List


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


class FullBinaryTreeFinder:
    def __init__(self) -> None:
        self.memo = {1: [TreeNode(0)]}

    def all_possible_trees(self, n: int) -> List["TreeNode"]:
        """Function to list all possible trees
        Args:
            n(int): an integer which means the all nodes number
        Returns:
            List["TreeNode"]: a list of all possible tree node
        """

        # brute force
        # time: O(N!)
        # space: O(N!)
        """
        ret = []

        if not n:
            return []
        
        if n == 1:
            return [TreeNode(0)]

        n -= 1

        for left_num in range(1, min(n, 20), 2):
            for left in self.all_possible_trees(left_num):
                for right in self.all_possible_trees(n - left_num):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ret.append(root)
        
        return ret
        """
    

        # recursion + memoization
        # time: O(2^N)
        # space: O(2^N)
        res = []
        if n in self.memo:
            return self.memo[n]
        
        if not n:
            return []

        n -= 1

        for left_num in range(1, min(n, 20), 2):
            for left in self.all_possible_trees(left_num):
                for right in self.all_possible_trees(n - left_num):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)

        self.memo[n + 1] = res

        return res