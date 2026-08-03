# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        
        queue = deque([root])
        d = 1

        while queue:
            if d == depth - 1:
                while queue:
                    node = queue.popleft()
                    node.left = TreeNode(val, node.left)
                    node.right = TreeNode(val, None, node.right)
                            
            curr_level_queue = queue
            next_level_queue = deque()
            while curr_level_queue:
                node = queue.popleft()
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
                
            queue = next_level_queue
            d += 1
        
        return root

