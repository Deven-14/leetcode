# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None:
            return head
        
        diff = right - left
        slow = fast = head

        while fast != None and diff > 0:
            fast = fast.next
            diff -= 1
        
        if slow == fast:
            return head
        
        i = 1
        slow_prev = None
        while i < left:
            slow_prev = slow
            slow = slow.next
            fast = fast.next
            i += 1
        fast_next = fast.next

        def reverse(start, end):
            curr = start
            new_head = None
            new_end = start
            while start != end:
                next = start.next
                start.next = new_head
                new_head = start
                start = next
            
            start.next = new_head
            new_head = start
            return new_head, new_end
        
        start, end = reverse(slow, fast)
        end.next = fast_next
        if slow_prev:
            slow_prev.next = start
            return head
        else:
            return start
