class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        count = 0

        while l < r:
            total = nums[l] + nums[r]
            if total == k:
                count += 1
                l += 1
                r -= 1
            elif total > k:
                r -= 1
            else:
                l += 1
        
        return count



class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        count = 0

        while l < r:
            total = nums[l] + nums[r]
            if total == k:
                count += 1
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1] and nums[r] == nums[r+1]:
                    count += 1
                    l += 1
                    r -= 1

            elif total > k:
                r -= 1
            else:
                l += 1
        
        return count


from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        max_pairs = 0

        for num in set(nums):
            rem = k-num
            if counts[rem] > 0:
                if num == rem:
                    max_pairs += counts[num] // 2
                else:
                    max_pairs += min(counts[num], counts[rem])
                
                del counts[num]
            
        return max_pairs


from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        max_pairs = 0

        for num in set(nums):
            rem = k-num
            if counts[rem] > 0:
                if num == rem:
                    max_pairs += counts[num] // 2
                else:
                    max_pairs += min(counts[num], counts[rem])
                
                counts[num] = 0
            
        return max_pairs


from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        max_pairs = 0

        for num in counts:
            rem = k-num
            if counts[rem] > 0:
                if num == rem:
                    max_pairs += counts[num] // 2
                else:
                    max_pairs += min(counts[num], counts[rem])
                
                counts[num] = 0
            
        return max_pairs