# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head.next
        fast = head.next.next

        while slow != fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if slow != fast:
            return None
        
        fast2 = head # fast2 is n (no of nodes in the cycles) ahead from the start
        while fast.next != slow:
            fast2 = fast2.next
            fast = fast.next
        
        slow2 = head # slow2 will reach the starting point when fast2.next == slow as fast2 is n times ahead of slow2
        while fast2.next != slow2:
            slow2 = slow2.next
            fast2 = fast2.next
        
        return slow2

# https://leetcode.com/problems/linked-list-cycle-ii/description/comments/1566045

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head.next
        fast = head.next.next

        while slow != fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if slow != fast:
            return None
        
        entry = head
        while entry != slow:
            slow = slow.next
            entry = entry.next
        
        return entry