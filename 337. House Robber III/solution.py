# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0, 0
            
            left_children_sum, left_grand_children_sum = dfs(root.left)
            right_children_sum, right_grand_children_sum = dfs(root.right)

            grand_children_sum = left_grand_children_sum + right_grand_children_sum

            return (
                root.val + grand_children_sum,
                max(
                    left_children_sum + right_children_sum, 
                    grand_children_sum,
                    left_children_sum + right_grand_children_sum,
                    right_children_sum + left_grand_children_sum,
                )
            )
        
        return max(dfs(root))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0, 0
            
            left_children_sum, left_grand_children_sum = dfs(root.left)
            right_children_sum, right_grand_children_sum = dfs(root.right)

            return (
                root.val + left_grand_children_sum + right_grand_children_sum,
                max(left_children_sum, left_grand_children_sum) + max(right_children_sum, right_grand_children_sum)
            )
        
        return max(dfs(root))