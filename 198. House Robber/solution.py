from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def helper(i):
            if i >= n:
                return 0
            
            return max(helper(i+1), nums[i]+helper(i+2))
        
        return helper(0)


from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[-1]

# I'm able to write dp solution using memoization method (using cache and backtracking) (first solution)