class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        max_theaft1 = [0] * n
        max_theaft1[0] = nums[0]
        max_theaft1[1] = max(nums[0], nums[1])

        for i in range(2, n-1):
            max_theaft1[i] = max(max_theaft1[i-1], max_theaft1[i-2] + nums[i])
        
        max_theaft2 = [0] * n
        max_theaft2[0] = 0
        max_theaft2[1] = nums[1]
        for i in range(2, n):
            max_theaft2[i] = max(max_theaft2[i-1], max_theaft2[i-2] + nums[i])
        
        return max(max_theaft1[-2], max_theaft2[-1])
