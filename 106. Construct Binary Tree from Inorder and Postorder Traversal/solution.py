# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        inorder_indices = {value: index for index, value in enumerate(inorder)}

        def divide_and_conquer(postorder_left, postorder_right, inorder_left, inorder_right):
            if postorder_left > postorder_right or inorder_left > inorder_right:
                return None

            val = postorder[postorder_right]
            idx = inorder_indices[val]
            node = TreeNode(val)
            n = idx - inorder_left
            node.left = divide_and_conquer(postorder_left, postorder_left+n-1, inorder_left, idx-1)
            node.right = divide_and_conquer(postorder_left+n, postorder_right-1, idx+1, inorder_right)

            return node
        
        return divide_and_conquer(0, n-1, 0, n-1)