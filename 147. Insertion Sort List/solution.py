# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(float('-inf'), head) 
        
        previous = new_head
        node = head
        while node:
            node.previous = previous
            previous = node
            node = node.next

        node = head
        while node:
            
            curr = node.previous
            while node.val < curr.val:
                curr = curr.previous
            
            if node.previous == curr:
                node = node.next
                continue
            
            node_previous = node.previous
            node_next = node.next
            node_previous.next = node_next
            if node_next:
                node_next.previous = node_previous

            curr_next = curr.next
            curr.next = node
            node.next = curr_next
            node.previous = curr
            curr_next.previous = node

            node = node_next
    
        return new_head.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(float('-inf'), head) 
        
        previous = new_head
        node = head
        while node:
            node.previous = previous
            previous = node
            node = node.next

        node = head
        while node:
            
            curr = node.previous
            if node.val > curr.val:
                node = node.next
                continue

            while node.val < curr.val:
                curr = curr.previous
            
            if node.previous == curr:
                node = node.next
                continue
            
            node_previous = node.previous
            node_next = node.next
            node_previous.next = node_next
            if node_next:
                node_next.previous = node_previous

            curr_next = curr.next
            curr.next = node
            node.next = curr_next
            node.previous = curr
            curr_next.previous = node

            node = node_next
    
        return new_head.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(float('-inf'), head) 
        
        node = head
        prev = new_head
        while node:
            
            if node.val >= prev.val:
                prev = node
                node = node.next
                continue

            curr = new_head.next
            curr_prev = new_head
            while node.val >= curr.val:
                curr_prev = curr
                curr = curr.next
            
            next = node.next
            prev.next = next

            node.next = curr
            curr_prev.next = node

            node = next

        return new_head.next
