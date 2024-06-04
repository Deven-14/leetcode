class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        n = len(nums)

        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        n = len(nums)

        while j < n:

            while j < n and nums[j] == val:
                j += 1
            
            while j < n and nums[j] != val:
                nums[i] = nums[j]
                i, j = i+1, j+1

        return i