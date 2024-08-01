# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if not root:
                return None
            
            if not root.left and not root.right:
                return root
            
            left_end = helper(root.left)
            right_end = helper(root.right)
            
            if left_end:
                left_end.right = root.right
                root.right = root.left
                root.left = None

            if right_end:
                return right_end
            else:
                return left_end
        
        helper(root)
        