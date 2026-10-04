class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        subset_total = total // k
        if any(num > subset_total for num in nums):
            return False

        n = len(nums)
        used = [False] * len(nums)

        @cache
        def backtrack(i, subset_sum, used):
            if i == k:
                return all(used)
            
            if subset_sum == subset_total:
                return backtrack(i + 1, 0, used)
            elif subset_sum > subset_total:
                return False
            
            used = list(used)
            for j in range(n):
                if used[j]:
                    continue
                used[j] = True
                if backtrack(i, subset_sum + nums[j], tuple(used)):
                    return True
                used[j] = False
            
            return False
        
        return backtrack(0, 0, tuple(used))