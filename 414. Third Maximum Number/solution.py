class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = nums[0], None, None
        
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num == first:
                continue
            elif second == None or num > second:
                third = second
                second = num
            elif num == second:
                continue
            elif third == None or num > third:
                third = num
                    
        return third if third != None else first