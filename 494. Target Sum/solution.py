from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def helper(i, total):
            if i == n:
                return int(total == target)
            
            return helper(i+1, total+nums[i]) + helper(i+1, total-nums[i])
        
        return helper(0, 0)
            

from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total < abs(target):
            return 0
        if (total + target) % 2 == 1:
            return 0

        @cache
        def helper(i, total):
            if i == n:
                return int(total == target)
            
            return helper(i+1, total+nums[i]) + helper(i+1, total-nums[i])
        
        return helper(0, 0)
            
# https://leetcode.com/problems/target-sum/solutions/97334/java-15-ms-c-3-ms-o-ns-iterative-dp-solution-using-subset-sum-with-explanation

#                   sum(P) - sum(N) = target
# sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
#                        2 * sum(P) = target + sum(nums)



from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total < abs(target):
            return 0
        if (total + target) % 2 == 1:
            return 0

        psum = (target + total) // 2
        dp = [0] * (psum + 1)
        dp[0] = 1

        for num in nums:
            for s in range(psum, num-1, -1):
                dp[s] += dp[s - num]

        return dp[psum]
            
# https://leetcode.com/problems/target-sum/solutions/97334/java-15-ms-c-3-ms-o-ns-iterative-dp-solution-using-subset-sum-with-explanation

#                   sum(P) - sum(N) = target
# sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
#                        2 * sum(P) = target + sum(nums)