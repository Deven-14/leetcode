# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []

        def inorder(root):
            if root == None:
                return
            
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)

        inorder(root)

        return values


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        values = []
        stack = []

        while node != None or stack:

            while node != None:
                stack.append(node)
                node = node.left
            
            if not stack:
                break
            
            curr = stack.pop()
            values.append(curr.val)
            node = curr.right
        
        return values
    


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        values = []
        stack = []

        while node or stack:

            while node:
                stack.append(node)
                node = node.left
            
            curr = stack.pop()
            values.append(curr.val)
            node = curr.right
        
        return values