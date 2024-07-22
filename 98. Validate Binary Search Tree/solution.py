# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def findMin(root):
            while root and root.left:
                root = root.left
            return root.val
        
        def findMax(root):
            while root and root.right:
                root = root.right
            return root.val

        def isValidBSTHelper(root, min, max):
            if root == None:
                return True
            
            if min < root.val < max:
                return isValidBSTHelper(root.left, min, root.val) and isValidBSTHelper(root.right, root.val, max)
            
            return False
        
        min, max = findMin(root), findMax(root)
        return isValidBSTHelper(root, min-1, max+1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(root, min, max):
            if root == None:
                return True
            
            if min < root.val < max:
                return isValidBSTHelper(root.left, min, root.val) and isValidBSTHelper(root.right, root.val, max)
            
            return False
        
        return isValidBSTHelper(root, float("-inf"), float("inf"))

