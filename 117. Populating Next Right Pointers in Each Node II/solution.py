"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = deque()
        queue.append(root)
        
        while queue:
            sub_queue = queue
            queue = deque()

            node = sub_queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            while sub_queue:
                next_node = sub_queue.popleft()
                node.next = next_node
                node = next_node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)    
                
        return root