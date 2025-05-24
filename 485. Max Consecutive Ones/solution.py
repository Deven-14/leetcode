class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_max_ones = 0
        for num in nums:
            if num == 1:
                curr_max_ones += 1
            else:
                max_ones = max(curr_max_ones, max_ones)
                curr_max_ones = 0
        
        max_ones = max(curr_max_ones, max_ones)
        return max_ones


# * instead of doing max function everytime in loop (which would be costly), run the max function at the end only ones by saving the results in a list
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones_count = []
        curr_max_ones = 0
        for num in nums:
            if num == 1:
                curr_max_ones += 1
            else:
                ones_count.append(curr_max_ones)
                curr_max_ones = 0
        
        ones_count.append(curr_max_ones)
        return max(ones_count)