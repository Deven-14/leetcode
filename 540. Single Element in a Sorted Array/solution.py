class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] != nums[l + 1]:
                return nums[l]
            
            if nums[r] != nums[r - 1]:
                return nums[r]
            
            mid = l + (r - l) // 2

            if (mid - l + 1) % 2 == 1:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 2
                elif nums[mid] == nums[mid - 1]:
                    r = mid - 2
                else:
                    return nums[mid]
            
            else:
                if nums[mid] == nums[mid + 1]:
                    r = mid - 1
                elif nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    return nums[mid]
        
        return nums[r]


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 2
                elif nums[mid] == nums[mid - 1]:
                    r = mid - 2
                else:
                    return nums[mid]
            
            else:
                if nums[mid] == nums[mid + 1]:
                    r = mid - 1
                elif nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    return nums[mid]
            
        return nums[r]

