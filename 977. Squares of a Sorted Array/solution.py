class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [num * num for num in nums]
        squares.sort()
        return squares


from bisect import bisect_left
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        i = bisect_left(nums, 0)
        if i == -1:
            pos_start = 0
            neg_start = -1
        else:
            pos_start = i
            neg_start = i-1
        
        n = len(nums)
        while neg_start >= 0 and pos_start < n:
            if nums[pos_start] <= abs(nums[neg_start]):
                squares.append(nums[pos_start] * nums[pos_start])
                pos_start += 1
            else:
                squares.append(nums[neg_start] * nums[neg_start])
                neg_start -= 1
        
        while pos_start < n:
            squares.append(nums[pos_start] * nums[pos_start])
            pos_start += 1
        
        while neg_start >= 0:
            squares.append(nums[neg_start] * nums[neg_start])
            neg_start -= 1
        
        return squares


from bisect import bisect_left
from heapq import merge
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = bisect_left(nums, 0)
        if i == -1 or i == 0:
            return [num * num for num in nums]
        
        neg = [num * num for num in nums[i-1::-1]]
        pos = [num * num for num in nums[i:]]
        return list(merge(pos, neg))
        