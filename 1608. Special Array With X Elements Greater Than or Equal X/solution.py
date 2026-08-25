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



