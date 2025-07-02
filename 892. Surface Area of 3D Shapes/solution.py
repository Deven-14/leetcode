class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total = 0
        n = len(grid)
                
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    total += 2
                    if i == 0:
                        total += grid[i][j]
                    elif grid[i-1][j] < grid[i][j]:
                        total += grid[i][j] - grid[i-1][j]
                    
                    if i == n-1:
                        total += grid[i][j]
                    elif grid[i+1][j] < grid[i][j]:
                        total += grid[i][j] - grid[i+1][j]
                    
                    if j == 0:
                        total += grid[i][j]
                    elif grid[i][j-1] < grid[i][j]:
                        total += grid[i][j] - grid[i][j-1]
                    
                    if j == n-1:
                        total += grid[i][j]
                    elif grid[i][j+1] < grid[i][j]:
                        total += grid[i][j] - grid[i][j+1]
        
        return total
                    