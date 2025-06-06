# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def preorder(root):
            if not root:
                return "$#"
            
            return f"${root.val}" + preorder(root.left) + preorder(root.right)
        
        return preorder(subRoot) in preorder(root)


# * INORDER WON'T WORK, as inorder of 2 trees shaped different can be the same for same values, better use preorder / postorder
# * USE SEPARATE SYMBOLS FOR INDICATING STARTING ($) AND NO NUMBER (#)