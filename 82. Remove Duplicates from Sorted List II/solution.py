# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        new_head = None
        prev = None
        curr = head

        while curr != None and curr.next != None:
            second = curr.next
            if curr.val == second.val:
                node = second.next
                val = curr.val
                
                while node != None and node.val == val:
                    node = node.next
                curr = node
                
            else:
                if not prev:
                    new_head = curr
                else:
                    prev.next = curr
                
                prev = curr
                prev.next = None
                curr = second
            
        if curr and curr.next == None:
            if prev:
                prev.next = curr
            else:
                new_head = curr
        
        return new_head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        new_head = ListNode() # dummy node
        prev = new_head
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                node = curr.next.next
                val = curr.val
                
                while node != None and node.val == val:
                    node = node.next
                curr = node
                
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
                prev.next = None
            
        if curr and curr.next == None:
            prev.next = curr
        
        return new_head.next
