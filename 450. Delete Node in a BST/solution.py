# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def smallestNode(self, root):
        if not root:
            return None
        
        node = root
        while node.left:
            node = node.left
        
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        
        if not root.left and not root.right:
            return None
        elif not root.right:
            return root.left
        elif not root.left:
            return root.right
        
        smallest_node = self.smallestNode(root.right)
        smallest_node.left = root.left
        return root.right
