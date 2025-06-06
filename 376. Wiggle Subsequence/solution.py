class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        if n == 2:
            return 2 if nums[0] != nums[1] else 1
        
        wiggle_seq = [nums[i] - nums[i-1] for i in range(1, n)]
        stack = [wiggle_seq[0]]
    
        for i in range(1, n-1):
            if (stack[-1] < 0 and wiggle_seq[i] > 0) or (stack[-1] > 0 and wiggle_seq[i] < 0):
                stack.append(wiggle_seq[i])
            else:
                stack[-1] += wiggle_seq[i]
        
        if stack[0] == 0:
            return 1

        return len(stack) + 1


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        if n == 2:
            return 2 if nums[0] != nums[1] else 1
        
        wiggle_seq = [nums[i] - nums[i-1] for i in range(1, n)]
        prev = wiggle_seq[0]
        length = 1
    
        for i in range(1, n-1):
            if (prev < 0 and wiggle_seq[i] > 0) or (prev > 0 and wiggle_seq[i] < 0):
                prev = wiggle_seq[i]
                length += 1
            else:
                prev += wiggle_seq[i]
            
        return length + 1 if prev != 0 else 1


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        if n == 2:
            return 2 if nums[0] != nums[1] else 1
        
        prev = nums[1] - nums[0]
        length = 1
    
        for i in range(2, n):
            wiggle = nums[i] - nums[i-1]
            if (prev < 0 and wiggle > 0) or (prev > 0 and wiggle < 0):
                prev = wiggle
                length += 1
            else:
                prev += wiggle
            
        return length + 1 if prev != 0 else 1


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        wiggle = None
        length = 1
    
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if (diff < 0 and wiggle != -1) or (diff > 0 and wiggle != 1):
                wiggle = 1 if diff > 0 else -1
                length += 1
            
        return length
