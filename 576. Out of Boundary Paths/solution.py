
# * 98%
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp(x, y, moves):
            if moves > maxMove:
                return 0
            
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            
            return (dp(x - 1, y, moves + 1) + dp(x + 1, y, moves + 1) + dp(x, y - 1, moves + 1) + dp(x, y + 1, moves + 1)) % MOD
        
        return dp(startRow, startColumn, 0)


# 99.33%
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp(x, y, moves):
            if moves > maxMove:
                return 0
            
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            
            reamining_moves = maxMove - moves
            if reamining_moves <= x and reamining_moves <= y and (x + reamining_moves) < m and (y + reamining_moves) < n:
                return 0
            
            return (dp(x - 1, y, moves + 1) + dp(x + 1, y, moves + 1) + dp(x, y - 1, moves + 1) + dp(x, y + 1, moves + 1)) % MOD
        
        return dp(startRow, startColumn, 0)


# Smart break: if you cannot reach the left, right, up, down from current pos (remain <= x && remain <=y && x+remain < m && y+remain < n) return 0. You are stuck in the middle