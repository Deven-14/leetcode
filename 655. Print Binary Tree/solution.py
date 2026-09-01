# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def dfs(node):
            if not node:
                return -1
            
            return 1 + max(dfs(node.left), dfs(node.right))
        
        height = dfs(root)
        m = height + 1
        n = 2 ** m  - 1

        matrix = [[""] * n for _ in range(m)]

        def dfsMatrix(node, r, c):
            if not node:
                return
            
            matrix[r][c] = str(node.val)
            h = 2 ** (height - r - 1)
            dfsMatrix(node.left, r + 1, c - h)
            dfsMatrix(node.right, r + 1, c + h)
        
        dfsMatrix(root, 0, (n - 1) // 2)
        return matrix