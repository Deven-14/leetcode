class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existing_numbers = {}
        for i, num in enumerate(nums):
            difference = target - num
            
            if difference in existing_numbers:
                return [existing_numbers[difference], i]
            
            existing_numbers[num] = i