# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        smallest_level = 1
        queue = deque([root])
        curr_level = 0

        while queue:
            sub_queue = queue
            queue = deque()
            curr_level += 1
            
            total = 0
            while sub_queue:
                node = sub_queue.popleft()
                total += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if total > max_sum:
                max_sum = total
                smallest_level = curr_level
        
        return smallest_level