from typing import Optional


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: "ListNode" = None
    ) -> None:
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode" = None,
        right: "TreeNode" = None
    ):
        self.val = val
        self.left = left
        self.right = right


class BSTMaker:
    def sorted_list_to_BST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        head: 1->2->3
        """
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)

        fast = slow = head
        prev = None

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        node = TreeNode(slow.val)
        second = slow.next
        prev.next = None

        node.right = self.sorted_list_to_BST(second)
        node.left = self.sorted_list_to_BST(head)

        return node


if __name__ == "__main__":
    print(BSTMaker().sorted_list_to_BST(ListNode(1, ListNode(2, ListNode(3)))).val)
