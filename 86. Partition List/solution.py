# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        if x < -100 or x > 100:
            return head
        
        slow = head
        slow_prev = None
        while slow != None and slow.val < x:
            slow_prev = slow
            slow = slow.next
        
        if slow == None:
            return head

        new_head = None
        if slow_prev == None:
            slow_prev = ListNode()
            new_head = slow_prev
            new_head.next = head

        fast = slow.next
        fast_prev = slow

        while fast != None:
            
            while fast != None and fast.val >= x:
                fast_prev = fast
                fast = fast.next
            
            if fast != None:
                next = fast.next
                fast.next = slow
                slow_prev.next = fast
                slow_prev = fast
                fast_prev.next = next
                fast = next
        
        if new_head == None:
            return head
        else:
            return new_head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        if x < -100 or x > 100:
            return head

        before_head = ListNode()
        before_node = before_head
        after_head = ListNode()
        after_node = after_head

        curr = head
        while curr != None:
            if curr.val < x:
                before_node.next = curr
                curr = curr.next
                before_node = before_node.next
            else:
                after_node.next = curr
                curr = curr.next
                after_node = after_node.next
        
        before_node.next = None
        after_node.next = None

        if before_head.next == None:
            return after_head.next
        elif after_head.next == None:
            return before_head.next
        
        before_node.next = after_head.next
        return before_head.next