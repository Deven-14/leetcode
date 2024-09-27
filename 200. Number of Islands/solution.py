class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        n_1, m_1 = n-1, m-1
        visited = [[False] * m for _ in range(n)]

        def visit_island(i, j):
            if visited[i][j]:
                return
            
            visited[i][j] = True

            if grid[i][j] == "0":
                return
            
            if i > 0:
                visit_island(i-1, j)
            if i < n_1:
                visit_island(i+1, j)
            if j > 0:
                visit_island(i, j-1)
            if j < m_1:
                visit_island(i, j+1)

        n_islands = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    continue
                
                if grid[i][j] == "0":
                    visited[i][j] = True
                    continue

                visit_island(i, j)
                n_islands += 1
        
        return n_islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        n_1, m_1 = n-1, m-1
        visited = [[False] * m for _ in range(n)]

        def visit_island(i, j):
            if visited[i][j]:
                return
            
            visited[i][j] = True

            if grid[i][j] == "0":
                return
            
            if i > 0:
                visit_island(i-1, j)
            if i < n_1:
                visit_island(i+1, j)
            if j > 0:
                visit_island(i, j-1)
            if j < m_1:
                visit_island(i, j+1)

        n_islands = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    visit_island(i, j)
                    n_islands += 1
                
                visited[i][j] = True
        
        return n_islands