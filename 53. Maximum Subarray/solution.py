class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_max = nums[0]
        curr_max = nums[0]
        for num in nums[1:]:
            curr_max = max(curr_max + num, num)
            sub_max = max(sub_max, curr_max)
        return sub_max


# divide and conquer method doesn't make sense here