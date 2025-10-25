class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed_list = []
        for freq, val in zip(nums[::2], nums[1::2]):
            decompressed_list.extend([val] * freq)
        return decompressed_list