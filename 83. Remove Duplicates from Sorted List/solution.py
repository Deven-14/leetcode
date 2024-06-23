# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        prev = head
        curr = head.next
        prev.next = None

        while curr != None:

            if curr.val != prev.val:
                prev.next = curr
                prev = curr
                curr = curr.next
                prev.next = None

            else:
                node = curr.next
                while node != None and prev.val == node.val:
                    node = node.next
                
                curr = node
        
        return head
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        prev = head
        curr = head.next
        prev.next = None

        while prev and curr:
            if prev.val != curr.val:
                prev.next = curr
                prev = curr
                curr = curr.next
            else:
                prev.next = None
                curr = curr.next
        
        return head
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
            
