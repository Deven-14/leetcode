class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return 
        
        n = len(nums)
        j = n-2

        while j > -1 and nums[j] >= nums[j+1]:
            j -= 1
        
        if j == -1:
            nums.reverse()
            return
        
        i = n-1
        while nums[i] <= nums[j]:
            i -= 1
        
        nums[i], nums[j] = nums[j], nums[i]

        k = j+1
        l = (n-k) // 2
        
        for m in range(l):
            nums[k+m], nums[-1-m] = nums[-1-m], nums[k+m]
        
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return 
        
        n = len(nums)
        j = n-2

        while j > -1 and nums[j] >= nums[j+1]:
            j -= 1
        
        if j == -1:
            nums.reverse()
            return
        
        i = n-1
        while nums[i] <= nums[j]:
            i -= 1
        
        nums[i], nums[j] = nums[j], nums[i] # swap

        k = j+1 # sort
        l = n-1

        while k < l:
            nums[k], nums[l] = nums[l], nums[k]
            k, l = k+1, l-1
