"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def helper(root):
            node = root

            while node.next:
                if node.child:
                    child_head, child_tail = helper(node.child)
                    node.child = None
                    next_node = node.next
                    child_head.prev = node
                    node.next = child_head
                    child_tail.next = next_node
                    next_node.prev = child_tail
                    node = child_tail
                
                node = node.next
            
            if node.child:
                child_head, child_tail = helper(node.child)
                child_head.prev = node
                node.next = child_head
                node.child = None
                node = child_tail

            return root, node
        
        if not head:
            return head
        
        helper(head)
        return head