class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        
        return f"{nums[0]}/({"/".join(str(num) for num in nums[1:])})"


#  @cache
# def backtrack(i, j):
#     if i == j:
#         return nums[i], f"{nums[i]}"
    
#     if i+1 == j:
#         return nums[i] / nums[j], f"({nums[i]}/{nums[j]})"

#     max_value = 0
#     operation = ""
#     for l in range(i+1, j):
#         numerator, numerator_operation = backtrack(i, l)
#         denominator, denominator_operation = backtrack(l + 1, j)
#         value = numerator / denominator
#         if value > max_value:
#             max_value = value
#             operation = f"({numerator_operation}/{denominator_operation})"
    
#     return max_value, operation