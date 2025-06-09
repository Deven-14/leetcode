# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        level_averages = []

        while queue:
            curr_level_queue = queue
            next_level_queue = deque()
            level_average = sum(x.val for x in curr_level_queue) / len(curr_level_queue)
            level_averages.append(level_average)

            while curr_level_queue:
                node = curr_level_queue.popleft()
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
            
            queue = next_level_queue
            
        return level_averages