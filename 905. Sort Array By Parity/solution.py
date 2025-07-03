class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1

        while i < n and nums[i] & 1 == 0:
            i += 1
            
        while j >= 0 and nums[j] & 1 == 1:
            j -= 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]

            while nums[i] & 1 == 0:
                i += 1
            
            while nums[j] & 1 == 1:
                j -= 1
        
        return nums
            