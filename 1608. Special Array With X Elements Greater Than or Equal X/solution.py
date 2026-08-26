import bisect
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        start, stop = 1, nums[-1] + 1
        
        for num in range(start, stop):
            idx = bisect.bisect_left(nums, num)
            if (n - idx) == num and nums[idx] >= num:
                return num

        return -1


import bisect
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        start, stop = 1, n + 1 # result has to be between [1, n]
        
        for num in range(start, stop):
            idx = bisect.bisect_left(nums, num)
            if (n - idx) == num and nums[idx] >= num:
                return num

        return -1


import bisect
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        i = 0
        
        while i < n and i < nums[i]: 
            i += 1
        
        return -1 if i < n and i == nums[i] else i


# i < nums[i] (in while loop so the negative condition of what we want)
# => i >= nums[i]
# => x >= nums[x]
# [4, 4, 3, 0, 0]
# 0 element >= nums[0] => 0 element >= 


