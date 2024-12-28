# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        path = []

        def helper(root):
            if not root:
                return
            
            path.append(str(root.val))
            helper(root.left)
            helper(root.right)

            if not root.left and not root.right:
                paths.append("->".join(path))
                
            path.pop()
        
        helper(root)
        return paths