# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def convert_linked_list_to_number(self, ll: Optional[ListNode]):
        node = ll
        num_list = []

        while node != None:
            num_list.append(str(node.val))
            node = node.next

        num_list.reverse()
        num = int("".join(num_list))
        return num
    
    def convert_number_to_linked_list(self, num: int):
        num_str = str(num)

        prev = None
        for i in num_str:
            prev = ListNode(int(i), prev)
        
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.convert_linked_list_to_number(l1)
        num2 = self.convert_linked_list_to_number(l2)

        total = num1 + num2

        l3 = self.convert_number_to_linked_list(total)
        return l3
