class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first = second = third = float("-inf")
        fourth = fifth = float("inf")

        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
            
            if num < fifth:
                fourth = fifth
                fifth = num
            elif num < fourth:
                fourth = num
        
        return max(first * second * third, first * fourth * fifth)
        
        