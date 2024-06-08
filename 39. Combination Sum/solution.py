# candidates not sorted, but this solution works for non sorted too as we are not breaking the for loop after the immediate larger number
class Solution:
    def backtrack(self, candidates, target, combinations, combination = [], total = 0, i = 0):
        if total > target:
            return
        
        if total == target:
            combinations.append(list(combination))
        
        for j in range(i, len(candidates)):
            combination.append(candidates[j])
            self.backtrack(candidates, target, combinations, combination, total+candidates[j], j)
            combination.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        self.backtrack(candidates, target, combinations)
        return combinations
    

# solution if the candidates are sorted, we can break the loop after the immediate larger number
class Solution:
    def backtrack(self, candidates, target, combinations, combination = [], total = 0, i = 0):
        if total == target:
            combinations.append(list(combination))
        
        for j in range(i, len(candidates)):
            if total+candidates[j] > target:
                break
            combination.append(candidates[j])
            self.backtrack(candidates, target, combinations, combination, total+candidates[j], j)
            combination.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        self.backtrack(candidates, target, combinations)
        return combinations