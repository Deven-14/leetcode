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


class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        subset_total = total // k
        if any(num > subset_total for num in nums):
            return False

        n = len(nums)
        used = 0

        @cache
        def backtrack(i, subset_sum, used):
            if i == k:
                return (used - ((1 << n) - 1)) == 0
            
            if subset_sum == subset_total:
                return backtrack(i + 1, 0, used)
            elif subset_sum > subset_total:
                return False 
            
            for j in range(n):
                if 1 << j & used:
                    continue
                used |= 1 << j
                if backtrack(i, subset_sum + nums[j], used):
                    return True
                used &= ~(1 << j)
            
            return False
        
        return backtrack(0, 0, used)

class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        subset_total = total // k
        if any(num > subset_total for num in nums):
            return False

        n = len(nums)
        used = 0

        nums.sort()

        @cache
        def backtrack(i, subset_sum, used):
            if i == k:
                return (used - ((1 << n) - 1)) == 0
            
            if subset_sum == subset_total:
                return backtrack(i + 1, 0, used)
            elif subset_sum > subset_total:
                return False 
            
            for j in range(n):
                if 1 << j & used:
                    continue
                if j > 0 and nums[j] == nums[j-1] and not (1 << (j-1) & used):
                    continue
                used |= 1 << j
                if backtrack(i, subset_sum + nums[j], used):
                    return True
                used &= ~(1 << j)
            
            return False
        
        return backtrack(0, 0, used)


class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        # early pruning
        nums.sort(reverse=True)
        
        target = total // k
        if nums[0] > target:
            return False

        n = len(nums)

        @cache
        def backtrack(subset_sum, used):
            if subset_sum == target:
                return backtrack(0, used)
            
            # all used 
            if used == (1 << n) - 1:
                return True
            
            if subset_sum == target:
                return backtrack(i + 1, 0, used)
            
            for j in range(n):
                # if used
                if (1 << j) & used:
                    continue
                
                if subset_sum + nums[j] > target:
                    continue
                
                # avoid duplicate choices
                if j > 0 and nums[j] == nums[j-1] and not (1 << (j-1) & used):
                    continue

                if backtrack(subset_sum + nums[j], used | (1 << j)):
                    return True
                
                if subset_sum == 0:
                    break
            
            return False
        
        return backtrack(0, 0)


class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        # early pruning
        nums.sort(reverse=True)
        
        target = total // k
        if nums[0] > target:
            return False

        n = len(nums)
        full_mask = (1 << n) - 1

        @cache
        def backtrack(subset_sum, used, start):
            if subset_sum == target:
                return backtrack(0, used, 0)
            
            # all used 
            if used == full_mask:
                return True
            
            if subset_sum == target:
                return backtrack(i + 1, 0, used)
            
            for j in range(start, n):
                # if used
                if (1 << j) & used:
                    continue
                
                if subset_sum + nums[j] > target:
                    continue
                
                # avoid duplicate choices
                if j > start and nums[j] == nums[j-1] and not (1 << (j-1) & used):
                    continue

                if backtrack(subset_sum + nums[j], used | (1 << j), j + 1):
                    return True
                
                if subset_sum == 0:
                    break
            
            return False
        
        return backtrack(0, 0, 0)


# 100 %
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        # early pruning
        nums.sort(reverse=True)
        
        target = total // k
        if nums[0] > target:
            return False

        n = len(nums)
        full_mask = (1 << n) - 1

        def backtrack(subset_sum, used, start):
            if subset_sum == target:
                return backtrack(0, used, 0)
            
            # all used 
            if used == full_mask:
                return True
            
            if subset_sum == target:
                return backtrack(i + 1, 0, used)
            
            for j in range(start, n):
                # if used
                if (1 << j) & used:
                    continue
                
                if subset_sum + nums[j] > target:
                    continue
                
                # avoid duplicate choices
                if j > start and nums[j] == nums[j-1] and not (1 << (j-1) & used):
                    continue

                if backtrack(subset_sum + nums[j], used | (1 << j), j + 1):
                    return True
                
                if subset_sum == 0:
                    break
            
            return False
        
        return backtrack(0, 0, 0)

    