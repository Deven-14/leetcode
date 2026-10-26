class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        count = 0
        l, r = 0, 0
        mul = 1
        
        while r < n:
            mul *= nums[r]

            while mul >= k and l <= r:
                mul //= nums[l]
                l += 1
            
            count += r - l + 1
            r += 1
        
        return count


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1: return 0
        
        n = len(nums)
        count = 0
        l, r = 0, 0
        mul = 1

        while r < n:
            mul *= nums[r]

            while mul >= k:
                mul //= nums[l]
                l += 1
            
            count += r - l + 1
            r += 1
        
        return count



class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1: return 0

        l = count = 0
        mul = 1

        for r in range(len(nums)):
            mul *= nums[r]

            while mul >= k:
                mul //= nums[l]
                l += 1
            
            count += r - l + 1
        
        return count

