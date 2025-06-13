class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 1
        max_l = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                l += 1
            else:
                max_l = max(max_l, l)
                l = 1
        
        max_l = max(max_l, l)
        return max_l


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 1
        lengths = [1]

        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                l += 1
            else:
                lengths.append(l)
                l = 1
        
        lengths.append(l)
        return max(lengths)

