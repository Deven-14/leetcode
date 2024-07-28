# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        inorder_indices = {value: index for index, value in enumerate(inorder)}

        def divide_and_conquer(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right or inorder_left > inorder_right:
                return None

            val = preorder[preorder_left]
            idx = inorder_indices[val]
            node = TreeNode(val)
            n = idx - inorder_left
            node.left = divide_and_conquer(preorder_left+1, preorder_left+n, inorder_left, idx-1)
            node.right = divide_and_conquer(preorder_left+n+1, preorder_right, idx+1, inorder_right)

            return node
        
        return divide_and_conquer(0, n-1, 0, n-1)


# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/comments/2095881