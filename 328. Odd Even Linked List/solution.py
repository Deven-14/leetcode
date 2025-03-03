# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd, even = head, head.next
        even_head = even
        while even and even.next:
            next_even = even.next.next
            odd.next = even.next
            even.next = next_even
            odd, even = odd.next, next_even
        
        odd.next = even_head
        return head