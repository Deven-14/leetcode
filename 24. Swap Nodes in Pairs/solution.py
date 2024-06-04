# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        first = head
        second = head.next
        
        first.next = second.next
        second.next = first
        head2 = second
        prev = first

        first = first.next
        while first:
            second = first.next
            if second == None:
                break
            
            first.next = second.next
            second.next = first
            prev.next = second
            
            prev = first
            first = first.next
        
        return head2
