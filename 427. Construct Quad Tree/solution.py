"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def helper(length, r, c):
            if length == 1:
                return Node(grid[r][c], True)
            
            half = length // 2
            topLeft = helper(half, r, c)
            topRight = helper(half, r, c + half)
            bottomLeft = helper(half, r + half, c)
            bottomRight = helper(half, r + half, c + half)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True)

            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return helper(len(grid), 0, 0)