from functools import cache
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        @cache
        def is_direct_decendent(root, node):
            if not root:
                return False
            
            if root == node:
                return True

            return is_direct_decendent(root.left, node) or is_direct_decendent(root.right, node)
        
        def indirect_decendent(root):
            if not root:
                return None
            
            if (is_direct_decendent(root.left, p) and is_direct_decendent(root.right, q)) or (is_direct_decendent(root.right, p) and is_direct_decendent(root.left, q)):
                return root
            
            return indirect_decendent(root.left) or indirect_decendent(root.right)
        
        if is_direct_decendent(p, q):
            return p
        elif is_direct_decendent(q, p):
            return q
        
        return indirect_decendent(root)
        
    
from functools import cache
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        
        return l or r