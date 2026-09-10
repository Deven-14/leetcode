# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def preorder(node):
            if not node:
                return None
            
            if node.val < low:
                return preorder(node.right)
            
            if node.val > high:
                return preorder(node.left)
            
            node.left = preorder(node.left)
            node.right = preorder(node.right)

            return node
        
        return preorder(root)