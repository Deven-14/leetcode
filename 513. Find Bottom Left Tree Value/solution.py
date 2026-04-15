# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        left_most_node = None

        while queue:
            curr_level_queue = queue
            next_level_queue = deque()
            left_most_node = queue[0]

            while curr_level_queue:
                node = curr_level_queue.popleft()
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
            
            queue = next_level_queue
        
        return left_most_node.val


