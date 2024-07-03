class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        sub_sets = [()]

        for num in nums:
            n = len(sub_sets)
            arr = (num,)
            for i in range(n):
                sub_sets.append(sub_sets[i] + arr)
            
        return set(sub_sets)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        sub_sets = [[]]
        subset = []

        def backtrack(i = 0):
            if i == n:
                return
            
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                
                subset.append(nums[j])
                sub_sets.append(list(subset))
                backtrack(j+1)
                subset.pop()
        
        backtrack()
            
        return sub_sets