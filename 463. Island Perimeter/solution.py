class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        LAST_ROW = n-1
        LAST_COL = m-1
        perimeter = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == LAST_ROW or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == LAST_COL or grid[i][j+1] == 0:
                    perimeter += 1
        
        return perimeter


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1: # check up
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1: # check left
                        perimeter -= 2
        
        return perimeter


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        perimeter = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1: # check up
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1: # check left
                        perimeter -= 2
        
        return perimeter
