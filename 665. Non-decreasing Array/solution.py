class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i, n = 1, len(nums)
        
        while i < n and nums[i] >= nums[i - 1]:
            i += 1
        
        if i == n: return True
        
        t = nums[i]
        nums[i] = nums[i - 1]
        j = i
        while j < n and nums[j] >= nums[j - 1]:
            j += 1
        
        if j == n: return True

        nums[i - 1] = nums[i] = t
        j = max(i - 1, 1)
        while j < n and nums[j] >= nums[j - 1]:
            j += 1
        
        return j == n
        
        