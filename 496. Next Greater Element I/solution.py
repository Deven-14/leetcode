class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[0]]
        greater = {}

        i, n = 1, len(nums2)
        while i < n:
            ele = nums2[i]
            while stack and ele > stack[-1]:
                greater[stack.pop()] = ele
            stack.append(ele)
            i += 1
        
        greater.update(dict.fromkeys(stack, -1))

        next_greater_nums = [greater[num] for num in nums1]
        return next_greater_nums

