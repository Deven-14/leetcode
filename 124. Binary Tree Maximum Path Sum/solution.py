# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        def postorder(node):
            if not node:
                return 0
            
            left_path_sum = postorder(node.left)
            right_path_sum = postorder(node.right)
            path_sum = max(
                node.val,
                left_path_sum + node.val,
                right_path_sum + node.val
            )
            nonlocal max_path_sum
            max_path_sum = max(
                max_path_sum, 
                path_sum,
                left_path_sum + node.val + right_path_sum
            )
            return path_sum
        
        postorder(root)
        return max_path_sum
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        def postorder(node):
            if not node:
                return 0
            
            left_path_sum = max(postorder(node.left), 0)
            right_path_sum = max(postorder(node.right), 0)

            nonlocal max_path_sum
            max_path_sum = max(
                max_path_sum, 
                left_path_sum + node.val + right_path_sum
            )

            return node.val + max(left_path_sum, right_path_sum)
        
        postorder(root)
        return max_path_sum
            



