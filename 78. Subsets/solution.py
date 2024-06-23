class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sub_sets = [[]]

        def backtrack(subset = [], i = 0):
            if i == n:
                return
            
            for j in range(i, n):
                subset.append(nums[j])
                sub_sets.append(list(subset))
                backtrack(subset, j+1)
                subset.pop()
        
        backtrack()
            
        return sub_sets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sub_sets = []
        subset = []

        def dfs(i = 0):
            if i == n:
                sub_sets.append(list(subset))
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs()
            
        return sub_sets


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sub_sets = [[]]
        subset = []

        for num in nums:
            n = len(sub_sets)
            arr = [num]
            for i in range(n):
                sub_sets.append(sub_sets[i] + arr)
            
        return sub_sets


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sub_sets = [[]]

        for num in nums:
            n = len(sub_sets)
            for i in range(n):
                subset = sub_sets[i].copy()
                subset.append(num)
                sub_sets.append(subset)
            
        return sub_sets