# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)

        def helper(node):
            if not node:
                return 0
            
            if not node.left and not node.right:
                freq[node.val] += 1
                return node.val
            
            left_sum = helper(node.left)
            right_sum = helper(node.right)
            sub_tree_sum = node.val + left_sum + right_sum
            freq[sub_tree_sum] += 1
            return sub_tree_sum

        helper(root)
        max_freq = max(freq.values())
        return [tree_sum for tree_sum, count in freq.items() if count == max_freq]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)

        def helper(node):
            if not node:
                return 0
            
            left_sum = helper(node.left)
            right_sum = helper(node.right)
            sub_tree_sum = node.val + left_sum + right_sum
            freq[sub_tree_sum] += 1
            return sub_tree_sum

        helper(root)
        max_freq = max(freq.values())
        return [tree_sum for tree_sum, count in freq.items() if count == max_freq]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)

        def helper(node):
            if not node:
                return 0
            
            sub_tree_sum = node.val + helper(node.left) + helper(node.right)
            freq[sub_tree_sum] += 1
            return sub_tree_sum

        helper(root)
        max_freq = max(freq.values())
        return [tree_sum for tree_sum, count in freq.items() if count == max_freq]
