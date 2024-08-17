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

# https://leetcode.com/problems/single-number-ii/solutions/3714928/bit-manipulation-c-java-python-beginner-friendly
# BIT MANIPULATOR SOLUITON


from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones ^= num & ~twos
            twos ^= num & ~ones
        
        return ones
