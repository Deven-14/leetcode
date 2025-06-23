# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        inf = float("inf")
        prev_val = inf
        
        def helper(node):
            if not node:
                return inf
            
            left_min_diff = helper(node.left)
            nonlocal prev_val
            min_diff = abs(node.val - prev_val)
            prev_val = node.val
            right_min_diff = helper(node.right)
            
            return min(left_min_diff, min_diff, right_min_diff)

        
        return helper(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        inf = float("inf")
        prev_val = inf
        min_diff = inf

        def helper(node):
            if not node:
                return 
            
            helper(node.left)
            nonlocal prev_val, min_diff
            min_diff = min(min_diff, abs(node.val - prev_val))
            prev_val = node.val
            helper(node.right)

        helper(root)
        return min_diff

