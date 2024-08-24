# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []

        def helper(root):
            if not root:
                return
            
            helper(root.left)
            helper(root.right)
            postorder.append(root.val)
        
        helper(root)
        return postorder


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []

        stack = []
        node = root
        while node or stack:

            while node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            
            curr = stack.pop()
            if stack and stack[-1] == curr.right:
                node = stack.pop()
                stack.append(curr)
            else:
                node = None
                postorder.append(curr.val)

        return postorder


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        postorder = []
        stack = [root]
        while stack:
            node = stack.pop()
            postorder.append(node.val) # second stack

            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
        
        return postorder[::-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        postorder = deque()
        stack = [root]
        while stack:
            node = stack.pop()
            postorder.appendleft(node.val) # second stack

            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
        
        return list(postorder)