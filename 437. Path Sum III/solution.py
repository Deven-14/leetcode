# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path_sums = []
        
        def helper(root):
            if not root:
                return 0
            
            count = 0
            for i in range(len(path_sums)):
                path_sums[i] += root.val
                if path_sums[i] == targetSum:
                    count += 1
                    
            path_sums.append(root.val)
            if path_sums[-1] == targetSum:
                count += 1
            
            count += helper(root.left)
            count += helper(root.right)

            path_sums.pop()
            for i in range(len(path_sums)):
                path_sums[i] -= root.val

            return count
        
        return helper(root)
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def helper(root, curr_path_sum, cache):
            if not root:
                return 0
            
            curr_path_sum += root.val
            sub_path_sum = curr_path_sum - targetSum
            
            count = cache[sub_path_sum]
            
            cache[curr_path_sum] += 1
            count += helper(root.left, curr_path_sum, cache)
            count += helper(root.right, curr_path_sum, cache)
            cache[curr_path_sum] -= 1

            return count
        
        cache = defaultdict(int)
        cache[0] = 1
        return helper(root, 0, cache)
            
