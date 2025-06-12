# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root.left:
            return -1
        
        if root.left.val != root.right.val:
            if root.left.val == root.val:
                left_min = self.findSecondMinimumValue(root.left)
                return min(left_min, root.right.val) if left_min != -1 else root.right.val
            else:
                right_min = self.findSecondMinimumValue(root.right)
                return min(right_min, root.left.val) if right_min != -1 else root.left.val
        
        left_min = self.findSecondMinimumValue(root.left)
        right_min = self.findSecondMinimumValue(root.right)
        if left_min == -1 and right_min == -1:
            return -1
        
        if left_min != -1 and right_min != -1:
            return min(left_min, right_min)
        
        return left_min if left_min != -1 else right_min
        