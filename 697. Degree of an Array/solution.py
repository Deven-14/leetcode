from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, last = {}, {}
        counts = {}

        for i, num in enumerate(nums):
            if num not in counts:
                first[num] = last[num] = i
                counts[num] = 1
            else:
                last[num] = i
                counts[num] += 1
        
        min_subarr_length = 0
        max_count = 0
        for num, count in counts.items():
            if count > max_count:
                min_subarr_length = last[num] - first[num] + 1
                max_count = count
            elif count == max_count:
                min_subarr_length = min(min_subarr_length, last[num] - first[num] + 1)
        
        return min_subarr_length


from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, last = {}, {}
        counts = {}

        for i, num in enumerate(nums):
            if num not in counts:
                first[num] = last[num] = i
                counts[num] = 1
            else:
                last[num] = i
                counts[num] += 1
        
        max_count = max(counts.values())
        min_subarr_length = min(
            last[num] - first[num] + 1
            for num in nums
            if counts[num] == max_count
        )
        
        return min_subarr_length


from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, last = {}, {}
        counts = Counter(nums)

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
        
        max_count = max(counts.values())
        min_subarr_length = min(
            last[num] - first[num] + 1
            for num in nums
            if counts[num] == max_count
        )
        
        return min_subarr_length


from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, last = {}, {}
        counts = defaultdict(int)
        min_subarr_length = len(nums)
        max_count = 0

        for i, num in enumerate(nums):
            first.setdefault(num, i)
            counts[num] += 1
            if counts[num] > max_count:
                min_subarr_length = i - first[num] + 1
                max_count = counts[num]
            elif counts[num] == max_count:
                min_subarr_length = min(
                    min_subarr_length,
                    i - first[num] + 1
                )
        
        return min_subarr_length


from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, last = {}, {}
        counts = Counter(nums)

        for i, num in enumerate(nums):
            first.setdefault(num, i)
            last[num] = i
        
        max_count = max(counts.values())
        min_subarr_length = min(
            last[num] - first[num] + 1
            for num in nums
            if counts[num] == max_count
        )
        
        return min_subarr_length