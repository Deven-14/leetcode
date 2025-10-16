# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        node = head
        num = 0

        while node:
            num <<= 1
            num |= node.val
            node = node.next
        
        return num