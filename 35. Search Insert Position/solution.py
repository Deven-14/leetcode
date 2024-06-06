class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        if target <= nums[left]:
            return 0
        
        if target > nums[right]:
            return right+1

        while left <= right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        if target > nums[mid]:
            return mid+1
        else:
            return mid