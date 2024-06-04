class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        n = len(nums)

        while j < n:
            
            while j < n and nums[j] == nums[i]:
                j += 1
            
            if j < n:
                i += 1
                nums[i] = nums[j]
                j += 1
        
        return i+1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        n = len(nums)

        while j < n:
            temp = nums[i]
            while j < n and nums[j] == temp:
                j += 1
            
            if j < n:
                i += 1
                nums[i] = nums[j]
                j += 1
        
        return i+1

