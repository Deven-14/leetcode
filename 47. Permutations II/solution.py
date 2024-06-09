class Solution:
    def backtrack(self, nums, permutations, start, stop):
        if start == stop:
            permutations.append(list(nums))
            return
        
        duplicate = set()
        for i in range(start, stop):
            if nums[i] in duplicate:
                continue
            duplicate.add(nums[i])
            nums[i], nums[start] = nums[start], nums[i]
            self.backtrack(nums, permutations, start+1, stop)
            nums[i], nums[start] = nums[start], nums[i]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        self.backtrack(nums, permutations, 0, n)
        return permutations        