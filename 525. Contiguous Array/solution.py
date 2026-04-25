class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if num == 0 else 1 for num in nums]
        accumulated_sums = list(accumulate(nums))
        seen = {0: -1}

        max_count = 0
        for i, num in enumerate(accumulated_sums):
            if num in seen:
                max_count = max(max_count, i - seen[num])
            else: # important - coz we want to only save the first occurrence
                seen[num] = i
        
        return max_count


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        max_count = 0
        if nums[0] == 1:
            seen[1] = 0
        else:
            nums[0] = -1
            seen[-1] = 0
        
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + (-1 if nums[i] == 0 else 1)
            if nums[i] in seen:
                max_count = max(max_count, i - seen[nums[i]])
            else: # important - coz we want to only save the first occurrence
                seen[nums[i]] = i
        
        return max_count
    

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        max_count = 0
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += -1 if nums[i] == 0 else 1
            if prefix_sum in seen:
                max_count = max(max_count, i - seen[prefix_sum])
            else: # important - coz we want to only save the first occurrence
                seen[prefix_sum] = i
        
        return max_count


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        max_count = 0
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += -1 if nums[i] == 0 else 1
            if prefix_sum in seen:
                if (t := i - seen[prefix_sum]) > max_count:
                    max_count = t
            else: # important - coz we want to only save the first occurrence
                seen[prefix_sum] = i
        
        return max_count


