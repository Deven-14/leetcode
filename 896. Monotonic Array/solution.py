class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        return all(nums[i] >= nums[i-1] for i in range(1, len(nums))) or all(nums[i] <= nums[i-1] for i in range(1, len(nums)))