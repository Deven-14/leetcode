# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0, 0
            
            lh, lm = dfs(node.left)
            rh, rm = dfs(node.right)

            return 1+max(lh, rh), max(lm, rm, lh + rh)
        
        max_depth, max_diameter = dfs(root)
        return max_diameter
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            lh = dfs(node.left)
            rh = dfs(node.right)
            nonlocal max_diameter
            max_diameter = max(max_diameter, lh + rh)

            return 1+max(lh, rh)
        
        dfs(root)
        return max_diameter