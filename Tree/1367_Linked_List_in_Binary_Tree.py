from collections import deque
from typing import Optional


class ListNode:
    def __init__(
            self, 
            val: int = 0, 
            next: Optional["ListNode"] = None
    ):
        self.val = val
        self.next = next


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
    def is_sub_path(
            self, 
            head: Optional[ListNode], 
            root: Optional[TreeNode]
    ) -> bool:
        queue = deque()
        queue.append(root)
        while queue:
            cur_tree = queue.popleft()
            if self.check_downward(head, cur_tree):
                return True
            
            if cur_tree.right:
                queue.append(cur_tree.right)
            
            if cur_tree.left:
                queue.append(cur_tree.left)

        return False
    
    def check_downward(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        
        if not root:
            return False
        
        if head.val != root.val:
            return False
        
        return self.check_downward(head.next, root.left) or self.check_downward(head.next, root.right)
