class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, count = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == num:
                count += 1
            elif count > 0:
                count -= 1
            else:
                num = nums[i]
                count = 1
        
        return num