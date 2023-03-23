"""
Given an integer n, return the number of structurally 
unique BST's (binary search trees) which has exactly n 
nodes of unique values from 1 to n.
"""
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int,
        left: Optional["TreeNode"],
        right: Optional["TreeNode"],
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class UniqueBSTNumber:
    def calc_unique_BST_num(n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            cur = 0
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                cur += left * right
            dp[i] = cur
        return dp[-1]


if __name__ == "__main__":
    ans = UniqueBSTNumber()
    ans.calc_unique_BST_num(3) 
