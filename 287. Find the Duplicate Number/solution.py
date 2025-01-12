class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = len(nums)
        if m == 1:
            return nums[0]
        
        slow = 0
        fast = 1

        while True:
            while nums[slow] != nums[fast]:
                slow = (slow + 1) % m
                fast = (fast + 2) % m
            
            if slow != fast:
                return nums[slow]
            
            fast = (fast + 1) % m


# time limit ecxceeded

# 2 pointers Floyd's Tortoise and Hare algorithm

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num = nums[0]
        slow = nums[num] # next[num]
        fast = nums[nums[num]] # next[next[num]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        start = nums[0]
        while start != slow:
            slow = nums[slow]
            start = nums[start]
        
        return start


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        v = nums[0]
        while v != nums[v]:
            nums[0], nums[v] = nums[v], nums[0]
            v = nums[0]
        
        return v