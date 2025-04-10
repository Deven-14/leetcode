# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def inorder(root, leaves):
            if not root:
                return 
            
            inorder(root.left, leaves)
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            inorder(root.right, leaves)
        
        root1_leaves = []
        root2_leaves = []

        inorder(root1, root1_leaves)
        inorder(root2, root2_leaves)
        return root1_leaves == root2_leaves