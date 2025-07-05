class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            if nums[idx] < 0:
                duplicates.append(abs(nums[i]))
            else:
                nums[idx] = -nums[idx]
        
        return duplicates


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num-1] < 0:
                duplicates.append(num)
            else:
                nums[num-1] *= -1
        
        return duplicates


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(len(nums)):
            num = abs(nums[i])
            idx = num - 1
            if nums[idx] < 0:
                duplicates.append(num)
            else:
                nums[idx] = -nums[idx]
        
        return duplicates