class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        combination = []
        
        def backtrack(i, start, stop):
            if i == k:
                combinations.append(list(combination))
                return

            for j in range(start, stop+1):
                combination.append(j)
                backtrack(i+1, j+1, stop+1)
                combination.pop()

        backtrack(0, 1, n-k+1)

        return combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        combination = []
        start, end = 1, n+1 # [start, end)
        stop = end-k+1
        
        def backtrack(i, a, b):
            if i == k:
                combinations.append(list(combination))
                return

            for j in range(a, b):
                combination.append(j)
                backtrack(i+1, j+1, b+1)
                combination.pop()

        backtrack(0, start, stop)

        return combinations

# list(combinations(range(1,n+1),k))