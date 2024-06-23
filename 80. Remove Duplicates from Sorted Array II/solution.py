class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)

        while j < n:

            prev = nums[j]
            nums[i] = nums[j]
            i += 1
            j += 1

            if j == n:
                break
            
            if prev == nums[j]:
                nums[i] = nums[j]
                i += 1
                j += 1
            
            while j < n and nums[j] == prev:
                j += 1
        
        return i
                