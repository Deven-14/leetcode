# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(root, max_val=float("-inf")):
            if not root:
                return 0
            
            count = 0
            if root.val >= max_val:
                count = 1
                max_val = root.val
            
            count += helper(root.left, max_val)
            count += helper(root.right, max_val)

            return count
        
        return helper(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(root, max_val):
            if not root:
                return 0
            
            count = 0
            if root.val >= max_val:
                count = 1
                max_val = root.val
            
            return count + helper(root.left, max_val) + helper(root.right, max_val)
        
        return helper(root, float("-inf"))



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(root, max_val):
            if not root:
                return 0
            
            if root.val >= max_val:
                return 1 + helper(root.left, root.val) + helper(root.right, root.val)
            
            return helper(root.left, max_val) + helper(root.right, max_val)
        
        return helper(root, float("-inf"))
