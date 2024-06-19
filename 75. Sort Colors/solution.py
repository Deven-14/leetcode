class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        counts = [0, 0, 0]

        for num in nums:
            counts[num] += 1
        
        nums[:counts[0]] = [0] * counts[0]

        nums[counts[0]:counts[0] + counts[1]] = [1] * counts[1]

        nums[counts[0] + counts[1]:] = [2] * counts[2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        i, j, k = 0, 0, n-1

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
