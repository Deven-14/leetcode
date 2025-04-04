from collections import deque
from itertools import groupby

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k == 0:
            lst = [len(list(g)) for k, g in groupby(nums) if k == 1]
            lst.append(0)
            return max(lst)

        queue = deque()

        i, j = -1, 0
        n = len(nums)
        max_ones = 0

        while j < n:

            if nums[j] == 0:
                if len(queue) == k:
                    i = queue.popleft()
                queue.append(j)
                
            max_ones = max(max_ones, j - i)
            j += 1
            
        return max_ones


from collections import deque
from itertools import groupby

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k == 0:
            lst = [len(list(g)) for k, g in groupby(nums) if k == 1]
            lst.append(0)
            return max(lst)

        queue = deque()

        i, j = -1, 0
        n = len(nums)
        max_ones = 0

        while j < n:

            if nums[j] == 0:
                if len(queue) == k:
                    i = queue.popleft()
                queue.append(j)
            
            diff = j-i
            if diff > max_ones:
                max_ones = diff
            j += 1
        
        return max_ones


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
        return right - left + 1