# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left, right):
            head = ListNode(0)
            node = head
            while left and right:

                while left and left.val <= right.val:
                    node.next = left
                    node = node.next
                    left = left.next
                
                if not left:
                    break

                while right and right.val <= left.val:
                    node.next = right
                    node = node.next
                    right = right.next
                
            while left:
                node.next = left
                node = node.next
                left = left.next
            
            while right:
                node.next = right
                node = node.next
                right = right.next
            
            return head.next

        def split(head):
            slow, fast, prev = head, head, None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            prev.next = None
            left_list = head
            right_list = slow

            return left_list, right_list
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            
            left_sub_list, right_sub_list = split(head)
            left = merge_sort(left_sub_list)
            right = merge_sort(right_sub_list)
            new_head = merge(left, right)
            
            return new_head

        return merge_sort(head)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left, right):
            head = ListNode(0)
            node = head
            while left and right:

                while left and left.val <= right.val:
                    node.next = left
                    node = node.next
                    left = left.next
                
                if not left:
                    break

                while right and right.val <= left.val:
                    node.next = right
                    node = node.next
                    right = right.next
                
            if left:
                node.next = left
            elif right:
                node.next = right
            
            return head.next

        def split(head):
            slow, fast, prev = head, head, None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            prev.next = None
            left_list = head
            right_list = slow

            return left_list, right_list
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            
            left_sub_list, right_sub_list = split(head)
            left = merge_sort(left_sub_list)
            right = merge_sort(right_sub_list)
            new_head = merge(left, right)
            
            return new_head

        return merge_sort(head)


# * ABOVE IS FASTER

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left, right):
            head = ListNode(0)
            node = head
            while left and right:
                if left.val <= right.val:
                    node.next = left
                    left = left.next
                else:
                    node.next = right
                    right = right.next
                node = node.next
            
            if left:
                node.next = left
            elif right:
                node.next = right
            
            return head.next

        def split(head):
            slow, fast, prev = head, head, None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            prev.next = None
            left_list = head
            right_list = slow

            return left_list, right_list
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            
            left_sub_list, right_sub_list = split(head)
            left = merge_sort(left_sub_list)
            right = merge_sort(right_sub_list)
            new_head = merge(left, right)
            
            return new_head

        return merge_sort(head)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left, right):
            head = ListNode(0)
            node = head
            while left and right:

                while left and left.val <= right.val:
                    node.next = left
                    node = node.next
                    left = left.next
                
                if not left:
                    break

                while right and right.val <= left.val:
                    node.next = right
                    node = node.next
                    right = right.next
                
            if left:
                node.next = left
            elif right:
                node.next = right
            
            return head.next

        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            left_list = head
            right_list = slow.next
            slow.next = None

            return left_list, right_list
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            
            left_sub_list, right_sub_list = split(head)
            left = merge_sort(left_sub_list)
            right = merge_sort(right_sub_list)
            new_head = merge(left, right)
            
            return new_head

        return merge_sort(head)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left, right):
            if not left:
                return right
            
            if not right:
                return left

            head = ListNode(0)
            node = head
            while left and right:

                while left and left.val <= right.val:
                    node.next = left
                    node = node.next
                    left = left.next
                
                if not left:
                    break

                while right and right.val <= left.val:
                    node.next = right
                    node = node.next
                    right = right.next
                
            node.next = left or right
            return head.next

        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            left_list = head
            right_list = slow.next
            slow.next = None

            return left_list, right_list
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            
            left_sub_list, right_sub_list = split(head)
            left = merge_sort(left_sub_list)
            right = merge_sort(right_sub_list)
            new_head = merge(left, right)
            
            return new_head

        return merge_sort(head)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left, right):
            if not left:
                return right
            
            if not right:
                return left

            head = ListNode(0)
            node = head
            while left and right:

                while left and left.val <= right.val:
                    node.next = left
                    node = left
                    left = left.next
                
                if not left:
                    break

                while right and right.val <= left.val:
                    node.next = right
                    node = right
                    right = right.next
                
            node.next = left or right
            return head.next

        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            left_list = head
            right_list = slow.next
            slow.next = None

            return left_list, right_list
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            
            left_sub_list, right_sub_list = split(head)
            left = merge_sort(left_sub_list)
            right = merge_sort(right_sub_list)
            new_head = merge(left, right)
            
            return new_head

        return merge_sort(head)


