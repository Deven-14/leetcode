# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = []
        nums2 = []

        node = l1
        while node:
            nums1.append(node.val)
            node = node.next
        
        node = l2
        while node:
            nums2.append(node.val)
            node = node.next
        
        carry = 0
        l3 = None
        while nums1 and nums2:
            carry, num = divmod(carry + nums1.pop() + nums2.pop(), 10)
            l3 = ListNode(num, l3)
        
        nums = nums1 or nums2
        while nums:
            carry, num = divmod(carry + nums.pop(), 10)
            l3 = ListNode(num, l3)
        
        if carry:
            l3 = ListNode(carry, l3)
        
        return l3
        