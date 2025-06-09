# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        count = 0
        randomNode = None

        while node != None:
            count += 1
            randomIndex = randint(0, count-1) # count-1 is inclusive
            if randomIndex == count-1:
                randomNode = node
            node = node.next
        
        return randomNode.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randrange
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        count = 0
        randomNode = None

        while node != None:
            count += 1
            randomIndex = randrange(0, count) # count is exclusive
            if randomIndex == count-1:
                randomNode = node
            node = node.next
        
        return randomNode.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randrange
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        count = 0
        randomNode = None

        while node != None:
            t = count
            count += 1
            randomIndex = randrange(0, count) # count is exclusive
            if randomIndex == t:
                randomNode = node
            node = node.next
        
        return randomNode.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import choice
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.values = []
        
        node = head
        while node:
            self.values.append(node.val)
            node = node.next

    def getRandom(self) -> int:
        return choice(self.values)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import choice
class Solution:

    def __init__(self, head: Optional[ListNode]):
        values = []
        
        node = head
        while node:
            values.append(node.val)
            node = node.next
        
        self.values = values

    def getRandom(self) -> int:
        return choice(self.values)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()