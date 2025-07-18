from bisect import bisect_left
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        length = bisect_left(nums, 0)
        if length == 0:
            if k % 2 == 1:
                return -nums[0] + sum(nums[1:])
            else:
                return sum(nums)
        
        if length == len(nums):
            if k <= len(nums):
                return -sum(nums)
            
            k -= len(nums)
            if k % 2 == 1:
                return -sum(nums[:-1]) + nums[-1]
            else:
                return -sum(nums)

        if k <= length:
            return -sum(nums[:k]) + sum(nums[k:])

        k -= length
        if k % 2 == 1:
            if abs(nums[length-1]) < nums[length]:
                return -sum(nums[:length-1]) + nums[length-1] + sum(nums[length:])
            else:
                return -sum(nums[:length]) + (-nums[length]) + sum(nums[length+1:])

        return -sum(nums[:length]) + sum(nums[length:])

