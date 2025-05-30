# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev_val = None
        min_diff = float("inf")

        def dfs(node):
            if not node:
                return
            dfs(node.left)

            nonlocal prev_val, min_diff
            if prev_val is None:
                prev_val = node.val
            else:
                min_diff = min(min_diff, node.val - prev_val)
                prev_val = node.val
            
            dfs(node.right)
        
        dfs(root)
        return min_diff
