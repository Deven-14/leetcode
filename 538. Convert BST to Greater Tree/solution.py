# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0 

        def postorder(node):
            if not node:
                return
            postorder(node.right)
            nonlocal total
            total += node.val
            node.val = total
            postorder(node.left)
            
        
        postorder(root)
        return root