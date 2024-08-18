"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node = head
        nodes = {}
        while node != None:
            nodes[node] = Node(node.val)
            node = node.next

        node = head
        while node != None:
            curr = nodes[node]
            if node.random:
                curr.random = nodes[node.random]
            if node.next:
                curr.next = nodes[node.next]
            node = node.next

        return nodes[head]


# * TOP ANSWER GAVE BETTER RESULTS

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node = head
        nodes = {}
        while node != None:
            nodes[node] = Node(node.val)
            node = node.next

        node = head
        nodes[None] = None
        while node != None:
            curr = nodes[node]
            curr.random = nodes[node.random]
            curr.next = nodes[node.next]
            node = node.next

        return nodes[head]