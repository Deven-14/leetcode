# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        
        n = 0
        node = head
        while node != None:
            n += 1
            node = node.next
        
        if n == 0 or n == 1:
            return head
        
        slow, fast = head, head

        i = 0
        k %= n
        if k == 0:
            return head
        
        while i < k:
            fast = fast.next
            i += 1
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head
        
