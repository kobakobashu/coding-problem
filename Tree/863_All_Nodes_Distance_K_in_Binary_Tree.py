from collections import defaultdict, deque
from typing import Dict, Optional, List


class TreeNode:
    def __init__(
            self, 
            x: int = 0,
            left: Optional["TreeNode"] = None,
            right: Optional["TreeNode"] = None,
    ):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_dict = self.make_adj_matrix(root)
        return self.find_k(adj_dict, target, k)

    def make_adj_matrix(self, root: TreeNode) -> Dict[int, set[int]]:
        adj_dict = defaultdict(set)
        queue = deque()
        queue.append([root, -1])
        while queue:
            cur, val = queue.popleft()
            if cur:
                if val >= 0:
                    adj_dict[val].add(cur.val)
                    adj_dict[cur.val].add(val)
                queue.append([cur.left, cur.val])
                queue.append([cur.right, cur.val])
        
        return adj_dict
        
    def find_k(self, adj_dict: Dict[int, set[int]], target: TreeNode, k: int):
        if target.val not in adj_dict:
            return []

        if k == 0:
            return [target.val] if target.val in adj_dict else []
        ans = []
        visited = set()
        queue = deque()
        queue.append(target.val)
        distance = 0
        while queue:
            n = len(queue)
            distance += 1
            for _ in range(n):
                cur = queue.popleft()
                visited.add(cur)
                for next_ele in adj_dict[cur]:
                    if next_ele in visited:
                        continue
                    
                    if distance == k:
                        ans.append(next_ele)
                    
                    else:
                        queue.append(next_ele)

        return ans
