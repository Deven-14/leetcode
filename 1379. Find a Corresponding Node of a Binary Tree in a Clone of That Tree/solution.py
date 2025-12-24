# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]

        while stack:
            node, cloned_node = stack.pop()
            if node == target:
                return cloned_node
            if node.right:
                stack.append((node.right, cloned_node.right))
            if node.left:
                stack.append((node.left, cloned_node.left))
        
        return None