from typing import Optional, List


class TreeNode:
    def __init__(
            self, 
            val: int = 0,
            left: Optional["TreeNode"] = None, 
            right: Optional["TreeNode"] = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def construct_from_pre_post(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        if not pre or not post:
            return None

        root = TreeNode(pre[0])
        if len(post) == 1:
            return root

        idx = pre.index(post[-2])
        root.left = self.construct_from_pre_post(pre[1: idx], post[:(idx - 1)])
        root.right = self.construct_from_pre_post(pre[idx: ], post[(idx - 1):-1])
        return root