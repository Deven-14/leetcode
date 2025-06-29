"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        level_order = []

        while queue:
            level = []
            curr_level_queue = queue
            next_level_queue = deque()

            while curr_level_queue:
                node = curr_level_queue.popleft()
                level.append(node.val)
                for child in node.children:
                    next_level_queue.append(child)
            
            queue = next_level_queue
            level_order.append(level)
        
        return level_order