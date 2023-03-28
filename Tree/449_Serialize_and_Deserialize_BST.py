from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left: Optional["TreeNode"] = None,
            right: Optional["TreeNode"] = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        node_list = []
        stack = deque()
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur:
                node_list.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        
        node_list = [str(node) for node in node_list]
        return " ".join(node_list)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        self.node_queue = deque(int(node) for node in data.split(" "))
        node = self.make_tree(float('-inf'), float('inf'))
        return node
    
    def make_tree(self, min_val, max_val) -> Optional[TreeNode]:
        if not self.node_queue:
            return None

        node_val = self.node_queue.popleft()
        if node_val <= min_val or max_val <= node_val:
            self.node_queue.appendleft(node_val)
            return None

        node = TreeNode(node_val)

        node.left = self.make_tree(min_val, node_val)
        node.right = self.make_tree(node_val, max_val)

        return node


if __name__ == "__main__":
    print(Codec().serialize(TreeNode(2, TreeNode(1), TreeNode(3))))
    print(Codec().deserialize("2 1 3"))