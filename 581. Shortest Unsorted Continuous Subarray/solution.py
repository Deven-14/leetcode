
# ! 70%
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        n = len(nums)
        count = n

        i = 0
        while i < n and nums_sorted[i] == nums[i]:
            i += 1
            count -= 1
        
        if i == n:
            return 0
        
        i = n-1
        while nums_sorted[i] == nums[i]:
            i -= 1
            count -= 1
        
        return count
        


# ! 20%

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)

        for i in range(n): # this is max O(2n) = O(n)
            while stack and nums[i] < nums[stack[-1]]:
                stack.pop()
            stack.append(i)
        
        if len(stack) == n:
            return 0
        
        start = 0
        m = len(stack)

        if stack[0] == 0:
            i = 1
            while i < m and stack[i] == stack[i-1] + 1:
                i += 1
            
            if i == m:
                return n - m
            
            start = i
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                stack.pop()
            stack.append(i)
        
        end = n-1
        m = len(stack)
        if stack[0] == end:
            i = 1
            while i < m and stack[i] == stack[i-1] - 1:
                i += 1
            
            if i == m:
                return n - m
        
            end = stack[i-1]-1
        
        return end - start + 1


# * 97%
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = float('-inf')
        min_num = float('inf')
        s = e = -1

        for i in range(n):
            if nums[i] >= max_num:
                max_num = nums[i]
            else:
                e = i
        
        for i in range(n-1, -1, -1):
            if nums[i] <= min_num:
                min_num = nums[i]
            else:
                s = i
        
        if s == -1 and e == -1:
            return 0

        return e - s + 1