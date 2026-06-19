class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_curr_sum = float('inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            min_curr_sum = min(min_curr_sum, curr_sum)
        
        return 1 if min_curr_sum > 0 else -min_curr_sum + 1

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_curr_sum = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            min_curr_sum = min(min_curr_sum, curr_sum)
        
        return 1 - min_curr_sum

