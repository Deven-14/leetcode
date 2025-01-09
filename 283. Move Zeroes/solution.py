class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        n = len(nums)
        while j < n:

            while j < n and nums[j] == 0:
                j += 1
            
            if j < n:
                nums[i] = nums[j]
                i += 1
            
            j += 1
        
        nums[i:] = [0] * (n-i)