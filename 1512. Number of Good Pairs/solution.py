from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        good_pairs = 0

        for count in counts.values():
            if count < 2:
                continue
            good_pairs += (count * (count - 1)) // 2 # n C 2 = n * (n - 1) / 2
        
        return good_pairs
