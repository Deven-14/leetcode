# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        elif root.right and not root.left:
            return 1 + self.minDepth(root.right)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # * BFS *****************************
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)
        level_order = []
        height = 0
        
        while queue:
            sub_queue = queue
            queue = deque()
            level = []
            height += 1

            while sub_queue:
                node = sub_queue.popleft()
                level.append(node.val)
                if not node.left and not node.right:
                    return height
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level_order.append(level)
        
        return level_order