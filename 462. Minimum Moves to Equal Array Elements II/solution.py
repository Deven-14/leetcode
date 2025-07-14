class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums) // 2
        mid = nums[i]
        return sum(mid - nums[i] for i in range(i)) + sum(nums[i] - mid for i in range(i, len(nums)))

