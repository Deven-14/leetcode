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

            return sum(dfs(kmoves - 1, x, y) for x, y in moves)
        
        return dfs(k, row, column) / 8 ** k
            
            
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = (
                (-2, -1),
                (-1, -2),
                (-2, +1),
                (-1, +2),
                (+2, -1),
                (+1, -2),
                (+2, +1),
                (+1, +2)
            )
        
        @cache
        def dfs(kmoves, i, j):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            
            if kmoves == 0:
                return 1
            
            return sum(dfs(kmoves - 1, i + dx, j + dy) for dx, dy in moves)
        
        return dfs(k, row, column) / 8 ** k
            
            
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = (
                (-2, -1),
                (-1, -2),
                (-2, +1),
                (-1, +2),
                (+2, -1),
                (+1, -2),
                (+2, +1),
                (+1, +2)
            )
        
        @cache
        def dfs(kmoves, i, j):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            
            if kmoves == 0:
                return 1
            
            return sum(dfs(kmoves - 1, i + dx, j + dy) for dx, dy in moves) * 0.125
        
        return dfs(k, row, column) 
            
            
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = (
                (-2, -1),
                (-1, -2),
                (-2, +1),
                (-1, +2),
                (+2, -1),
                (+1, -2),
                (+2, +1),
                (+1, +2)
            )
        
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            next_dp = [[0.0] * n for _ in range(n)]

            for i in range(n):
                r = dp[i]
                for j in range(n):
                    val = r[j]
                    
                    if val == 0:
                        continue
                    
                    p = dp[i][j] / 8
                    for dx, dy in moves:
                        x, y = i + dx, j + dy
                        if x < 0 or x >= n or y < 0 or y >= n:
                            continue
                        next_dp[x][y] += p

            dp = next_dp
        
        return sum(sum(row) for row in dp)
