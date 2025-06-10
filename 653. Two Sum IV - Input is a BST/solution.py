# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()

        def inorder(node):
            if not node:
                return False
            
            if inorder(node.left):
                return True
            if (k - node.val) in nums:
                return True

            nums.add(node.val)
            return inorder(node.right)

        return inorder(root)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        stack = [root]

        while stack:
            node = stack.pop()
            if (k - node.val) in nums:
                return True
            nums.add(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return False
