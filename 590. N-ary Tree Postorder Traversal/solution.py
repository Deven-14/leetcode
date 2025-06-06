"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        postorder_list = []

        def helper(root):
            if not root:
                return
            
            for child in root.children:
                helper(child)
            postorder_list.append(root.val)
        
        helper(root)
        return postorder_list


"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        postorder_list = []
        stack = [root]

        while stack:
            node = stack.pop()
            postorder_list.append(node.val)
            stack.extend(node.children)
        
        return postorder_list[::-1]


"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        postorder_list = deque()
        stack = [root]

        while stack:
            node = stack.pop()
            postorder_list.appendleft(node.val)
            stack.extend(node.children)
        
        return postorder_list