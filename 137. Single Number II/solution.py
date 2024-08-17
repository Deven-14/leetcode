from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if counts[num] == 3:
                del counts[num]
        
        return list(counts.keys())[0]


from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        for num in nums:
            if counts[num] == 1:
                return num

# * instead of defaultdict we could use Counter also

