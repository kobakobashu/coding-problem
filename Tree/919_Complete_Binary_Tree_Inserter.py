from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        cur = root
        queue = deque()
        queue.append(root)
        self.wait_queue = deque()
        while queue:
            cur = queue.popleft()
            if cur.left and cur.right:
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                self.wait_queue.append(cur)

    def insert(self, val: int) -> int:
        next_queue = self.wait_queue.popleft()
        if not next_queue.left:
            next_queue.left = TreeNode(val)
            self.wait_queue.appendleft(next_queue)
            self.wait_queue.append(next_queue.left)
        else:
            next_queue.right = TreeNode(val)
            self.wait_queue.append(next_queue.right)
        return next_queue.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
