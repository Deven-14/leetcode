class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        greater = [-1] * n

        for i in range(len(nums)):
            ele = nums[i]
            while stack and ele > nums[stack[-1]]:
                greater[stack.pop()] = ele
            stack.append(i)
        
        for i in range(len(nums)):
            ele = nums[i]
            while stack and ele > nums[stack[-1]]:
                greater[stack.pop()] = ele
                
        return greater
