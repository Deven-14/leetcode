class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        @cache
        def dfs(kmoves, i, j):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            
            if kmoves == 0:
                return 1
            
            moves = (
                (i - 2, j - 1),
                (i - 1, j - 2),
                (i - 2, j + 1),
                (i - 1, j + 2),
                (i + 2, j - 1),
                (i + 1, j - 2),
                (i + 2, j + 1),
                (i + 1, j + 2)
            )

            prob = [dfs(kmoves - 1, x, y) for x, y in moves]
            return sum(prob) / 8
        
        return dfs(k, row, column)
            
            
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        @cache
        def dfs(kmoves, i, j):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            
            if kmoves == 0:
                return 1
            
            moves = (
                (i - 2, j - 1),
                (i - 1, j - 2),
                (i - 2, j + 1),
                (i - 1, j + 2),
                (i + 2, j - 1),
                (i + 1, j - 2),
                (i + 2, j + 1),
                (i + 1, j + 2)
            )

            return sum(dfs(kmoves - 1, x, y) for x, y in moves) / 8
        
        return dfs(k, row, column)
            
            
