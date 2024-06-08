class Solution:
    def backtrack(self, candidates, target, combinations, combination = [], total = 0, i = 0):
        if total == target:
            combinations.append(list(combination))
        
        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j-1]:
                continue
            
            if total+candidates[j] > target:
                break
            
            combination.append(candidates[j])
            self.backtrack(candidates, target, combinations, combination, total+candidates[j], j+1)
            combination.pop()
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        self.backtrack(candidates, target, combinations)
        return combinations