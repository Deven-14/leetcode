class Solution:
    def search_leftmost(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return idx
    
    def search_rightmost(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                idx = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return idx
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                leftmost = self.search_leftmost(nums, target, left, mid)
                rightmost = self.search_rightmost(nums, target, mid, right)
                return [leftmost, rightmost]
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return [-1, -1]