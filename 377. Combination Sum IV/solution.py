from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        @cache
        def helper(i, total):
            if i == n:
                return 0
            
            if total == target:
                return 1
            
            combinations = 0
            for j in range(i, n):
                if total + nums[j] > target:
                    break
                combinations += helper(i, total + nums[j])

            return combinations
        
        return helper(0, 0)


from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        @cache
        def helper(total):
            if total == target:
                return 1
            
            combinations = 0
            for i in range(n):
                if total + nums[i] > target:
                    break
                combinations += helper(total + nums[i])

            return combinations
        
        return helper(0)


from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        @cache
        def helper(total):
            if total == 0:
                return 1
            
            combinations = 0
            for i in range(n):
                if nums[i] > total:
                    break
                combinations += helper(total - nums[i])

            return combinations
        
        return helper(target)


from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1 # 1 way to get total as 0, select nothing

        for total in range(1, target + 1):
            for num in nums:
                if num <= total:
                    dp[total] += dp[total - num]
        
        return dp[target]


from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1 # 1 way to get total as 0, select nothing
        nums.sort()

        for total in range(1, target + 1):
            for num in nums:
                if num > total:
                    break
                
                dp[total] += dp[total - num]
        
        return dp[target]


