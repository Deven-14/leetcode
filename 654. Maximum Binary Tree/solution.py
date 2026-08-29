# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        left_node = None

        for num in nums:
            while stack and num > stack[-1].val:
                left_node = stack.pop()
            
            new_node = TreeNode(num)
            if left_node:
                new_node.left = left_node
                left_node = None
            if stack:
                pnode = stack[-1]
                pnode.right = new_node
            stack.append(new_node)
        
        return stack[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = [TreeNode(1001)]
        left_node = None

        for num in nums:
            while num > stack[-1].val:
                left_node = stack.pop()
            
            new_node = TreeNode(num)
            if left_node:
                new_node.left = left_node
                left_node = None
            pnode = stack[-1]
            pnode.right = new_node
            stack.append(new_node)
        
        return stack[0].right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = [TreeNode(1001)]
        left_node = None

        for num in nums:
            new_node = TreeNode(num)
            while num > stack[-1].val:
                new_node.left = stack.pop()
            
            stack[-1].right = new_node
            stack.append(new_node)
        
        return stack[0].right


