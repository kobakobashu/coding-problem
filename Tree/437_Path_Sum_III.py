from collections import deque
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


class PathSum:
    def path_finder(self, root: Optional[TreeNode], target_sum: int) -> int:
        ans = 0
        stack = deque()
        stack.append([root, [root.val]])
        while stack:
            node, cur_sum = stack.pop()
            ans += cur_sum.count(target_sum)
            if node.left:
                stack.append([node.left, [x + node.left.val for x in cur_sum] + [node.left.val]])
            if node.right:
                stack.append([node.right, [x + node.right.val for x in cur_sum] + [node.right.val]])
        
        return ans


if __name__ == "__main__":
    print(PathSum().path_finder(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(2))), 8))