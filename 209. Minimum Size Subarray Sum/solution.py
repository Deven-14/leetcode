class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        sum = 0
        
        length = 0
        min_length = n+1
        while i < n:
            if sum < target:
                sum += nums[i]
                length += 1
                i += 1

            elif j < i:
                min_length = min(min_length, length)
                sum -= nums[j]
                length -= 1
                j += 1
            
            else:
                return 1
        
        while j < i and sum >= target:
            min_length = min(min_length, length)
            sum -= nums[j]
            length -= 1
            j += 1
            
        return min_length if min_length != n+1 else 0


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        sum = 0
        length = 0
        min_length = n+1
        
        while i < n:
            while i < n and sum < target:
                sum += nums[i]
                length += 1
                i += 1

            while j < i and sum >= target:
                min_length = min(min_length, length)
                sum -= nums[j]
                length -= 1
                j += 1
            
            if min_length == 1:
                return 1
            
        return min_length if min_length != n+1 else 0
        