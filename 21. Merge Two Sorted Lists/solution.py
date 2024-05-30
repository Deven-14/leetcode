# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1
        
        node1, node2 = list1, list2
        head = ListNode() # dummy node
        node3 = head

        while node1 and node2:
            if node1.val <= node2.val:
                node3.next = node1
                node1 = node1.next
            else:
                node3.next = node2
                node2 = node2.next
            node3 = node3.next
        
        if node1:
            node3.next = node1
        elif node2:
            node3.next = node2
        
        head = head.next # removing dummy node
        return head
