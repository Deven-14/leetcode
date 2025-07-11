class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s3 = float("-inf")
        stack = []

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < s3:
                return True
            
            while stack and nums[i] > stack[-1]:
                s3 = stack.pop()
            
            stack.append(nums[i])
        
        return False


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s3 = float("-inf")
        stack = [float("inf")]

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < s3:
                return True
            
            while nums[i] > stack[-1]:
                s3 = stack.pop()
            
            stack.append(nums[i])
        
        return False


# https://leetcode.com/problems/132-pattern/solutions/94071/single-pass-c-o-n-space-and-time-solution-8-lines-with-detailed-explanation