# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []

        def helper(root):
            if not root:
                return
            
            preorder.append(root.val)
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return preorder


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        preorder = []
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            preorder.append(node.val)
            
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        
        return preorder