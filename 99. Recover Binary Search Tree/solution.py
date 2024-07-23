"""
There are only two cases
case 1:
    The violated pairs are adjacent to each other
    1 2 3 4 5 6 7
    1 3 2 4 5 6 7 (3 and 2)
    [(3,2)]

case 2:
    The violated pairs are not adjacent to each other
    1 2 3 4 5 6 7
    1 6 3 4 5 2 7 (6 and 2)
    [(6,3), (5,2)]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        violated_pairs = []
        prev = None

        def inorder(root):
            nonlocal prev
            if root == None:
                return
            
            inorder(root.left)
            if prev and prev.val > root.val:
                violated_pairs.append((prev, root))
            prev = root
            inorder(root.right)
        
        inorder(root)

        def get_violated_pair():
            if len(violated_pairs) == 1:
                return violated_pairs[0]
            else:
                return violated_pairs[0][0], violated_pairs[1][1]
        
        first, second = get_violated_pair()
        first.val, second.val = second.val, first.val

# https://leetcode.com/problems/recover-binary-search-tree/solutions/5334376/simple-python-solution-with-o-1-space-complexity/