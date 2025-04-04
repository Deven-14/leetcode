class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ones = 0
        j = -1
        last_zero_idx = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                j = last_zero_idx
                last_zero_idx = i

            max_ones = max(max_ones, i-j-1)
        
        return max_ones


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ones = 0
        start = 0
        last_zero_idx = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                start = last_zero_idx + 1
                last_zero_idx = i

            max_ones = max(max_ones, i - start)
        
        return max_ones
