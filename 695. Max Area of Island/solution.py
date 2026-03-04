class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0

            if visited[i][j] or grid[i][j] == 0:
                return 0
            
            visited[i][j] = True
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(area, max_area)
        
        return max_area


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0

            if visited[i][j] or grid[i][j] == 0:
                return 0
            
            visited[i][j] = True
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(area, max_area)
        
        return max_area
