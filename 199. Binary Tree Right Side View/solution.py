from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_nodes = []
        node = root
        queue = deque([node])

        while queue:
            ele = queue[-1]
            right_nodes.append(ele.val)
            sub_queue = queue
            queue = deque()
            
            while sub_queue:
                node = sub_queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_nodes