class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        i, j = 0, len(nums) - 1
        start, end = 0, 0
        while i <= j:
            if end <= start:
                end += nums[j]
                j -= 1
            else:
                start += nums[i]
                i += 1
        
        if end <= start:
            j -= 1
        
        if j == -1:
            return nums[::-1]
        
        return nums[:j:-1]
        
