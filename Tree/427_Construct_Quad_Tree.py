from typing import Optional, List


class Node:
    def __init__(
        self,
        val: int,
        isLeaf: bool,
        topLeft: Optional["Node"] = None, 
        topRight: Optional["Node"] = None,
        bottomLeft: Optional["Node"] = None,
        bottomRight: Optional["Node"] = None
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Constructer:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if self.is_leaf(grid):
            return Node(grid[0][0], True)
        
        mid = len(grid) // 2
        return Node(
            "*",
            False,
            self.construct([row[:mid] for row in grid[:mid]]),
            self.construct([row[mid:] for row in grid[:mid]]),
            self.construct([row[:mid] for row in grid[mid:]]), 
            self.construct([row[mid:] for row in grid[mid:]])
        )
    
    def is_leaf(self, grid: List[List[int]]) -> bool:
        if not grid:
            return True

        pre = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != pre:
                    return False
        
        return True
        