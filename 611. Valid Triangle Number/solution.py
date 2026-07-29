from bisect import bisect_left
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        @cache
        def find(ele, start):
            return bisect_left(nums, ele, start)
        
        n = len(nums)
        count = 0

        for i in range(n-2):
            for j in range(i + 1, n-1):
                sum_of_2_sides = nums[i] + nums[j]
                idx = find(sum_of_2_sides, j + 1)
                count += idx - (j + 1)
        
        return count
    

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n-1, -1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        
        return count


