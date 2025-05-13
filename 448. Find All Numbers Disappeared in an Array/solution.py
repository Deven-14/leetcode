class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)

        nums = [num-1 for num in nums]

        while i < n:
            t = nums[i]
            nums[t], nums[i] = t, nums[t]
            if nums[i] == t:
                i += 1

        ans = [i+1 for i, num in enumerate(nums) if i != num]
        return ans


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)

        while i < n:
            t = nums[i]-1
            if t == i or nums[t] == nums[i]:
                i += 1
            else:
                nums[t], nums[i] = nums[i], nums[t]

        ans = [i for i, num in enumerate(nums, start=1) if i != num]
        return ans


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in s]

