# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def preorder(node):
            if not node:
                return ""
            
            if not node.left and not node.right:
                return f"{node.val}"
            elif not node.right:
                return f"{node.val}({preorder(node.left)})"
            elif not node.left:
                return f"{node.val}()({preorder(node.right)})"
            
            return f"{node.val}({preorder(node.left)})({preorder(node.right)})"
        
        return preorder(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def preorder(node):
            if not node.left and not node.right:
                return f"{node.val}"
            elif not node.right:
                return f"{node.val}({preorder(node.left)})"
            elif not node.left:
                return f"{node.val}()({preorder(node.right)})"
            
            return f"{node.val}({preorder(node.left)})({preorder(node.right)})"
        
        return preorder(root)

