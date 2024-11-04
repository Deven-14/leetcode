class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []

        def helper(i=0, j=1, combination=[], total=0):
            if k == i:
                if total == n:
                    combinations.append(list(combination))
                return
            
            for l in range(j, 10):
                if l + total > n:
                    return
                combination.append(l)
                helper(i+1, l+1, combination, total+l)
                combination.pop()
        
        helper()

        return combinations
                
