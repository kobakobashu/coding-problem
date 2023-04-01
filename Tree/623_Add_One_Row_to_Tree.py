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


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        
        node = root
        queue = deque()
        queue.append([node, 1])
        while queue:
            n = len(queue)
            for _ in range(n):
                cur, cur_depth = queue.popleft()
                if cur:
                    queue.append([cur.left, cur_depth + 1])
                    queue.append([cur.right, cur_depth + 1])

                    if cur_depth == depth - 1:
                        tmp = cur.left
                        cur.left = TreeNode(val, tmp)

                        tmp = cur.right
                        cur.right = TreeNode(val, None, tmp)

        return root


if __name__ == "__main__":
    print()