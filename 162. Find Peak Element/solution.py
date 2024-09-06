class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        
        if nums[-1] > nums[-2]:
            return n-1

        l, r = 1, n-2
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid+1] > nums[mid]:
                l = mid+1
            elif nums[mid-1] > nums[mid]:
                r = mid-1