# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        max_len = 0
        
        def dfs(node):
            left, right = 0, 0

            if node.left:
                l = dfs(node.left)
                if node.left.val == node.val:
                    left = l + 1
            
            if node.right:
                r = dfs(node.right)
                if node.right.val == node.val:
                    right = r + 1
            
            nonlocal max_len
            max_len = max(max_len, left + right)

            return max(left, right)
        
        dfs(root)
        return max_len