class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_1st_n_numbers = (n * (n + 1)) // 2
        sum_nums = sum(nums)
        return sum_of_1st_n_numbers - sum_nums