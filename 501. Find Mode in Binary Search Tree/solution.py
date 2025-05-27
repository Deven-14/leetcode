# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = defaultdict(int)

        def inorder(root):
            if not root:
                return 0

            left_mode = inorder(root.left)
            modes[root.val] += 1
            right_mode = inorder(root.right)

            return max(modes[root.val], left_mode, right_mode)

        mode = inorder(root)
        
        return [ele for ele, count in modes.items() if count == mode]


# ! slower
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = defaultdict(int)
        counts_to_eles = defaultdict(set)

        def inorder(root):
            if not root:
                return 0

            left_mode = inorder(root.left)
            modes[root.val] += 1
            counts_to_eles[modes[root.val]].add(root.val)
            right_mode = inorder(root.right)

            return max(modes[root.val], left_mode, right_mode)

        mode = inorder(root)
        
        return list(counts_to_eles[mode])



# * nonlocal is important, it is very HELPFUL
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = []
        mode = 0
        curr_val = None
        count = 0

        def inorder(root):
            if not root:
                return 0

            inorder(root.left)
            
            nonlocal mode, curr_val, count
            if root.val == curr_val:
                count += 1
            else:
                curr_val = root.val
                count = 1
            
            if count > mode:
                mode = count
                modes.clear()
                modes.append(curr_val)
            elif count == mode:
                modes.append(curr_val)

            inorder(root.right)

        inorder(root)
        
        return modes