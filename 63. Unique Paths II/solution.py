class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[1] * n for _ in range(m)]

        grid[0][0] = 0
        value = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                value = 0
            grid[0][j] = value
        
        value = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                value = 0
            grid[i][0] = value

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[m-1][n-1]