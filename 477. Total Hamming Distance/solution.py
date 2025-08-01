class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        hd = 0
        bin_nums = (f"{num:032b}" for num in nums)
        for bits in zip(*bin_nums):
            hd += bits.count('0') * bits.count('1')
        
        return hd


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bin_nums = (f"{num:032b}" for num in nums)
        hd = sum(bits.count('0') * bits.count('1') for bits in zip(*bin_nums))        
        return hd