# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0, 0

            lsum, ltilt = dfs(root.left)
            rsum, rtilt = dfs(root.right)
            return root.val + lsum + rsum, ltilt + rtilt + abs(lsum - rsum)
        
        _, tilt = dfs(root)
        return tilt


# * we can also use nonlocal tilt and then keep adding and return that

