# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root, parent_value=""):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return int(parent_value + str(root.val))
            
            value = parent_value + str(root.val)
            left_value = helper(root.left, value)
            right_value = helper(root.right, value)
            return left_value + right_value
        
        return helper(root)