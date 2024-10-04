# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode()
        new_head = temp

        node = head
        while node:
            if node.val != val:
                temp.next = node
                temp = temp.next
            node = node.next
        
        temp.next = None

        return new_head.next