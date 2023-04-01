from collections import defaultdict
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


class SubtreeFinder:
    def find_duplicate_subtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.from_triplet_to_id = dict()
        self.cnt = defaultdict(int)
        self.res = []
        self.traverse(root)
        return self.res
    
    def traverse(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        triplet = (self.traverse(node.left), node.val, self.traverse(node.right))
        if triplet not in self.from_triplet_to_id:
            self.from_triplet_to_id[triplet] = len(self.from_triplet_to_id) + 1
        
        id = self.from_triplet_to_id[triplet]
        self.cnt[id] += 1
        if self.cnt[id] == 2:
            self.res.append(node)

        return id
