from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        
        @cache
        def dfs(i, j):
            max_path = 1
            for x, y in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                
                if matrix[x][y] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(x, y))
            
            return max_path
        
        max_path = max(
            dfs(i, j)
            for i in range(n)
            for j in range(m)
        )

        return max_path
    

from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        
        @cache
        def dfs(i, j):
            ele = matrix[i][j]
            return 1 + max(
                dfs(i + 1, j) if i + 1 < n and ele < matrix[i+1][j] else 0,
                dfs(i - 1, j) if i - 1 >= 0 and ele < matrix[i-1][j] else 0,
                dfs(i, j + 1) if j + 1 < m and ele < matrix[i][j+1] else 0,
                dfs(i, j - 1) if j - 1 >= 0 and ele < matrix[i][j-1] else 0
            )

        return max(dfs(i, j) for i in range(n) for j in range(m))
    

