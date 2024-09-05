# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = set()

        node = headA
        while node:
            nodes.add(node)
            node = node.next
        
        node = headB
        while node and node not in nodes:
            node = node.next
        
        return node


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA_start = headA
        nodeB_start = headB
        nodeA = headA
        nodeB = headB

        while nodeA and nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        if nodeA:
            while nodeA:
                nodeA_start = nodeA_start.next
                nodeA = nodeA.next
        
        if nodeB:
            while nodeB:
                nodeB_start = nodeB_start.next
                nodeB = nodeB.next
        
        nodeA = nodeA_start
        nodeB = nodeB_start

        while nodeA and nodeB and nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        return nodeA
