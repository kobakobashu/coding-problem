from collections import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class NArrayPostorder:
    def postorder(self, root: 'Node') -> List[int]:
        self.ans = []
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root:
            return
            
        for child in root.children:
            self.dfs(child)
        
        self.ans.append(root.val)
        return