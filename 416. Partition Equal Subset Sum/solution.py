from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def helper(i, sum1, sum2):
            if i == n:
                return sum1 == sum2
            
            return helper(i+1, sum1+nums[i], sum2) or helper(i+1, sum1, sum2+nums[i])

        return helper(0, 0, 0)


# ! memory limit exceeded


from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        n = len(nums)
        half = total // 2

        @cache
        def helper(i, sum1):
            if i == n:
                return False
            
            if sum1 == half:
                return True
            
            return helper(i+1, sum1+nums[i]) or helper(i+1, sum1)

        return helper(0, 0)


# 21%

from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        n = len(nums)
        half = total // 2
        nums.sort()

        @cache
        def helper(i, sum1):
            if i == n:
                return False
            
            if sum1 == half:
                return True
            elif sum1 > half:
                return False
            
            return helper(i+1, sum1+nums[i]) or helper(i+1, sum1)

        return helper(0, 0)

# * 86%

from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        n = len(nums)
        half = total // 2
        nums.sort()

        @cache
        def helper(i, sum1):
            if i == n:
                return False
            
            if sum1 == half:
                return True
            elif sum1 > half:
                return False
            
            return helper(i+1, sum1+nums[i]) or helper(i+1, sum1)

        return helper(0, 0)