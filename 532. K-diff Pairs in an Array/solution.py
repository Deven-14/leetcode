from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        pairs = 0
        
        if k == 0:
            return sum(1 for num in counts if counts[num] > 1)

        for num in list(counts):
            diff = k + num
            if diff in counts:
                pairs += 1
        
        return pairs
    

from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        pairs = 0
        
        if k == 0:
            return sum(1 for num in counts if counts[num] > 1)

        for num in counts:
            diff = k + num
            if diff in counts:
                pairs += 1
        
        return pairs


from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        
        if k == 0:
            return sum(1 for num in counts if counts[num] > 1)

        return sum(1 for num in counts if (k + num) in counts)