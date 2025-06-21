class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = second = float("-inf")
        idx = -1

        for i, num in enumerate(nums):
            if num > largest:
                idx = i
                second = largest
                largest = num
            elif num > second:
                second = num
        
        return idx if largest >= 2 * second else -1