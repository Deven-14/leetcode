# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # reverse second half
        prev = None
        node = slow
        while node:
            next = node.next
            node.next = prev
            prev, node = node, next
        
        middle = prev
        start = head
        max_twin_sum = 0
        while middle:
            max_twin_sum = max(max_twin_sum, middle.val + start.val)
            start, middle = start.next, middle.next
        
        return max_twin_sum


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow, fast = slow.next, fast.next.next
        
        max_twin_sum = 0
        while slow:
            max_twin_sum = max(max_twin_sum, stack.pop() + slow.val)
            slow = slow.next
        
        return max_twin_sum