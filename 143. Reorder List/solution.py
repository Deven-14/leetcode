# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        stack = []
        node = head
        while node != None:
            stack.append(node)
            node = node.next
        
        curr = head
        node = stack.pop()
        while curr != node and curr.next != node:
            next = curr.next
            node.next = next
            curr.next = node
            curr = next
            node = stack.pop()
        
        node.next = None

