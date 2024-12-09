# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthNode = None

        def helper(root, k):
            if not root:
                return 0, None
            
            nleft, node = helper(root.left, k)
            if node:
                return nleft, node
            
            if nleft+1 == k:
                return k, root
            
            nright, node = helper(root.right, k-nleft-1)
            if node:
                return nright, node
            
            return nleft+nright+1, None
        
        k2, node = helper(root, k)
        return node.val