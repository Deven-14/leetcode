"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        preorder_list = []

        def helper(root):
            if not root:
                return
            
            preorder_list.append(root.val)
            for child in root.children:
                helper(child)
        
        helper(root)
        return preorder_list
    


"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
            
        preorder_list = []

        node = root
        stack = [node]

        while stack:
            node = stack.pop()
            preorder_list.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        
        return preorder_list
    

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        preorder_list = []

        node = root
        stack = [node]

        while stack:
            node = stack.pop()
            preorder_list.append(node.val)
            stack.extend(node.children[::-1])
        
        return preorder_list