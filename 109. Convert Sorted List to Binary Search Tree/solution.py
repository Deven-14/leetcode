# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def helper(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid-1)
            node.right = helper(mid+1, right)

            return node

        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        
        return helper(0, len(nums)-1)