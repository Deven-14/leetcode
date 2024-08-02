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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
            
            node.next = None
        
        return root



# * since bfs is iterative, it is better than dfs in this case


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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        def dfs(root):
            if not root.left and not root.right:
                return root
            
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return root