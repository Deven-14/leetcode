class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_grid = [[0] * n for _ in range(m)]

        min_grid[0][0] = grid[0][0]

        for j in range(1, n):
            min_grid[0][j] = min_grid[0][j-1] + grid[0][j]

        for i in range(1, m):
            min_grid[i][0] = min_grid[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                min_grid[i][j] = grid[i][j] + min(min_grid[i-1][j], min_grid[i][j-1])
        
        return min_grid[m-1][n-1]