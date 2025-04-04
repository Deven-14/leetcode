class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        if 0 == right_sum-nums[0]:
            return 0
        
        right_sum -= nums[0]
        for i in range(1, len(nums)):
            left_sum += nums[i-1]
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i
        
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        
        return -1