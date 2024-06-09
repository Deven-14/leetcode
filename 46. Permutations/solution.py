class Solution:
    def backtrack(self, nums, n, permutations, visited, permutation=[]):
        if n == len(permutation):
            permutations.append(list(permutation))
            return
        
        for i in range(n):
            if visited[i] == True:
                continue
            visited[i] = True
            permutation.append(nums[i])
            self.backtrack(nums, n, permutations, visited, permutation)
            permutation.pop()
            visited[i] = False

    def backtrack2(self, nums, permutations, start, stop):
        if start == stop:
            permutations.append(list(nums))
            return
        
        for i in range(start, stop): # always think in terms of indices as this is permutation and it doesn't depend on the value but the index
            nums[i], nums[start] = nums[start], nums[i]
            self.backtrack2(nums, permutations, start+1, stop)
            nums[i], nums[start] = nums[start], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # visited = [False] * n
        permutations = []
        # self.backtrack(nums, n, permutations, visited)
        self.backtrack2(nums, permutations, 0, n)
        return permutations