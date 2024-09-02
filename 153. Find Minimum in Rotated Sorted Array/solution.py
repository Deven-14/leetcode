class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i+j) // 2
            if nums[i] < nums[mid] < nums[j]:
                return nums[i]
            elif nums[i] < nums[mid]:
                i = mid
            elif nums[mid] < nums[j]:
                j = mid
            else:
                return nums[j]

# both solutions are good, mine gave better resut, should check with runtime which is actuallly betters

class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        return nums[i]