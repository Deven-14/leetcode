# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if not root:
                return 0
            
            lh = helper(root.left)
            rh = helper(root.right)

            if abs(lh-rh) > 1:
                raise Exception
            
            return 1+max(lh, rh)
        
        try:
            helper(root)
            return True
        except:
            return False


# EXCEPTION ONE GAVE BETTER RESULTS THAN BELOW SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if not root:
                return 0
            
            lh = helper(root.left)
            rh = helper(root.right)

            if lh == -1 or rh == -1 or abs(lh-rh) > 1:
                return -1
            
            return 1+max(lh, rh)
        
        return helper(root) != -1