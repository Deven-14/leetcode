import bisect
class Solution:
    def binary_search_reverse(self, nums):
        target = 0
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                l = mid + 1
            else:
                r = mid
        
        return l

    def countNegatives(self, grid: List[List[int]]) -> int:
        i = len(grid) - 1
        j = self.binary_search_reverse(grid[-1])
        n = len(grid[-1])

        print(j)
        if j == n:
            return 0

        count = (n - j)
        i -= 1
        while i >= 0 and j < n:

            nums = grid[i]
            while j < n and nums[j] >= 0: # could do this search also through reverse binary search
                j += 1

            if j == n:
                return count 

            count += (n - j)
            i -= 1

        return count


# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/comments/1576437/