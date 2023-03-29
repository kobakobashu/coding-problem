from collections import deque
from typing import List


class Node:
    def __init__(self, val: int = None, children: List["Node"] = []):
        self.val = val
        self.children = children


class NArrayPreorder:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        node = root
        stack = deque()
        stack.append(node)
        while stack:
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                for child in cur.children[::-1]:
                    stack.append(child)
        
        return ans


if __name__ == "__main__":
    print(NArrayPreorder().preorder(Node(1, [Node(2, [Node(5), Node(6)]), Node(3), Node(4)])))