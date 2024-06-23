class Solution:
    def binary_serach(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return False
    
    def search(self, nums: List[int], target: int) -> bool:    
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            
            if left == mid:
                left = mid + 1
            elif nums[left] == nums[mid]:
                if nums[mid] == nums[right]:
                    j = left + 1
                    ele = nums[left]
                    while j < mid and ele == nums[j]:
                        j += 1
                    if j == mid:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return self.binary_serach(nums, target, left, mid-1)
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    return self.binary_serach(nums, target, mid+1, right)
                else:
                    right = mid-1

        return False 
    

class Solution:
    def binary_serach(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return False
    
    def search(self, nums: List[int], target: int) -> bool:    
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return self.binary_serach(nums, target, left, mid-1)
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    return self.binary_serach(nums, target, mid+1, right)
                else:
                    right = mid-1

        return False