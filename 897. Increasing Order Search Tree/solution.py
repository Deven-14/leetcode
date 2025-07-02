# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        new_head = TreeNode()
        node = new_head

        def inorder(root):
            if not root:
                return None
            
            inorder(root.left)
            nonlocal node
            node.right = root
            node = node.right
            root.left = None
            inorder(root.right)
        
        inorder(root)
        return new_head.right