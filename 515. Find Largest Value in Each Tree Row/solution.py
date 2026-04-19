# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

TreeNode.__gt__ = lambda self, other: self.val > other.val

from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        max_in_rows = []

        while queue:
            max_in_rows.append(max(queue).val)
            curr_level_queue = queue
            next_level_queue = deque()

            while curr_level_queue:
                node = curr_level_queue.popleft()
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
            
            queue = next_level_queue
        
        return max_in_rows

