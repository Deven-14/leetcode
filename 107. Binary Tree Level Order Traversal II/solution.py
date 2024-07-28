# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        level_order = []
        
        while queue:
            sub_queue = queue
            queue = deque()
            level = []

            while sub_queue:
                node = sub_queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level_order.append(level)
        
        return level_order[::-1]