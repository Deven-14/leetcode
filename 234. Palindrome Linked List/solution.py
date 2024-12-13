# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        node = slow.next
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        
        tail = prev
        while tail and head.val == tail.val:
            head = head.next
            tail = tail.next
        
        return not tail

# this is O(n) time complexity solution that uses O(1) space complexity
