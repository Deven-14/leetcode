# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, parent):
            if not root:
                return 0
            
            if not root.left and not root.right and parent and parent.left == root:
                return root.val
            
            total = helper(root.left, root)
            total += helper(root.right, root)
            return total
        
        return helper(root, None)