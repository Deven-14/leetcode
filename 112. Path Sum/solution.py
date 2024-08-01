# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root, total=0):
            if not root:
                return False
            
            total = total + root.val
            if not root.left and not root.right:
                return total == targetSum

            return helper(root.left, total) or helper(root.right, total)
        
        return helper(root)