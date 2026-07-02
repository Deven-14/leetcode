class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest, second_largest = 0, 0
        for num in nums:
            if num > largest:
                largest, second_largest = num, largest
            elif num > second_largest:
                second_largest = num
        return (largest - 1) * (second_largest - 1)
