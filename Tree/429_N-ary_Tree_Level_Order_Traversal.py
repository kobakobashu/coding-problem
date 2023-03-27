from collections import deque
from typing import List


class Node:
    def __init__(
        self,
        val: int = None,
        children: List["Node"] = None
    ):
        self.val = val
        self.children = children


class NodeLevelOrder:
    def level_order(self, root: Node) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        queue = deque()
        queue.append(root)
        while queue:
            cur_level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    cur_level.append(cur.val)
                    for child in cur.children:
                        queue.append(child)
            
            ans.append(cur_level)
        
        return ans
