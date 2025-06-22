from itertools import groupby
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        seq = []
        for i in range(1, len(nums)):
            seq.append(nums[i] - nums[i-1])
        
        total = 0
        for k, g in groupby(seq):
            l = list(g)
            n = len(l)
            if n > 1:
                m = n + 1 # no of eles
                total += (m * (m + 1)) // 2 - m - (m-1) # -m for subsets len 1, -(m-1) for subsets len 2
        
        return total


# ans = 0
# cur_sum = 0

# for i in range(2, n):
#     if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
#         cur_sum += 1
#         ans += cur_sum
#     else:
#         cur_sum = 0