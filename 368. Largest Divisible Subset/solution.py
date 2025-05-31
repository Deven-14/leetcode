from functools import cache
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            divisible_subsets = [0]

            for j in range(i):
                if nums[i] % nums[j] == 0:
                    divisible_subsets.append(dp[j])
            
            dp[i] += max(divisible_subsets)
        
        max_idx, max_div_subsets = max(enumerate(dp), key=lambda x: x[1])
        num = nums[max_idx]
        largest_div_subset = [num]
        max_div_subsets -= 1

        for i in range(max_idx-1, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_div_subsets:
                num = nums[i]
                max_div_subsets -= 1
                largest_div_subset.append(num)
        
        return largest_div_subset
    


from functools import cache
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_idx = 0

        for i in range(1, n):
            divisible_subsets = [0]

            for j in range(i):
                if nums[i] % nums[j] == 0:
                    divisible_subsets.append(dp[j])
            
            dp[i] += max(divisible_subsets)
            if dp[max_idx] < dp[i]:
                max_idx = i
        
        max_div_subsets = dp[max_idx]
        num = nums[max_idx]
        largest_div_subset = [num]
        max_div_subsets -= 1

        for i in range(max_idx-1, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_div_subsets:
                num = nums[i]
                max_div_subsets -= 1
                largest_div_subset.append(num)
        
        return largest_div_subset


from functools import cache
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_idx = 0

        for i in range(1, n):
            divisible_subsets = [0]

            for j in range(i):
                if nums[i] % nums[j] == 0:
                    divisible_subsets.append(dp[j])
            
            dp[i] += max(divisible_subsets)
            if dp[max_idx] < dp[i]:
                max_idx = i
        
        max_div_subsets = dp[max_idx]
        num = nums[max_idx]
        largest_div_subset = [num]
        max_div_subsets -= 1

        for i in range(max_idx-1, -1, -1):
            if dp[i] == max_div_subsets and num % nums[i] == 0:
                num = nums[i]
                max_div_subsets -= 1
                largest_div_subset.append(num)
        
        return largest_div_subset


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        subsets = [[num] for num in nums]

        for i in range(1, n):
            subset = subsets[i]
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(subsets[i]) < len(subsets[j]) + 1:
                    subsets[i] = subset + subsets[j]
        
        return max(subsets, key=len)

        
        