# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        path = []

        def helper(root, total=0):
            if not root:
                return
            
            path.append(root.val)
            total = total + root.val
            if not root.left and not root.right and total == targetSum:
                paths.append(list(path))

            helper(root.left, total)
            helper(root.right, total)
            path.pop()
        
        helper(root)
        return paths