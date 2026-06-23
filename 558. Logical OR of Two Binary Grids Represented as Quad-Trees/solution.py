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
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if not quadTree1 or not quadTree2:
            return quadTree1 or quadTree2
        
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val | quadTree2.val, True, None, None, None, None)
        
        if (quadTree1.isLeaf and quadTree1.val) or (quadTree2.isLeaf and quadTree2.val):
            return Node(True, True, None, None, None, None)

        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        if (topLeft.val | topLeft.val and
            topRight.val | topRight.val and
            bottomLeft.val | bottomLeft.val and
            bottomRight.val | bottomRight.val):
            return Node(True, True, None, None, None, None)

        quadTree3 = Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        return quadTree3
        
        