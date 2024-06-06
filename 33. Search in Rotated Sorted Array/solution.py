class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2 # mid = left + (right-left) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        return -1


class Solution:            
    def search(self, nums: list[int], target: int) -> int:        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        return -1


class Solution:
    def binary_serach(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1
            
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2 # mid = left + (right-left) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    return self.binary_serach(nums, target, left, mid-1)
                else:
                    left = mid+1
            else:
                if target > nums[mid] and target <= nums[right]:
                    return self.binary_serach(nums, target, mid+1, right)
                else:
                    right = mid-1

        return -1


class Solution:
    def binary_serach(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1
    
    def search(self, nums: list[int], target: int) -> int:        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]: # check if left is sorted
                if nums[left] <= target < nums[mid]:
                    return self.binary_serach(nums, target, left, mid-1)
                else:
                    left = mid+1
            else: # otherwise, right is sorted
                if nums[mid] < target <= nums[right]:
                    return self.binary_serach(nums, target, mid+1, right)
                else:
                    right = mid-1

        return -1