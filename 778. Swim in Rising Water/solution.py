
# ! timeout 
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        INF = float('inf')
        visited = [[False] * m for _ in range(n)]
        
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or visited[i][j]:
                return INF

            if i == n-1 and j == m-1:
                return grid[i][j]

            min_level = INF
            visited[i][j] = True
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                min_level = min(min_level, dfs(x, y))

            visited[i][j] = False
            return max(
                grid[i][j], 
                min_level
            )
        
        return dfs(0, 0)
        

# * Dijkstra's Algorithm - kinda

import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        INF = float('inf')
        min_times = [[INF] * m for _ in range(n)]
        min_times[0][0] = grid[0][0]
        min_heap = [(grid[0][0], 0, 0)]

        while min_heap:
            curr_time, i, j = heapq.heappop(min_heap)
            if curr_time > min_times[i][j]:
                continue
            
            if i == n-1 and j == m-1:
                return curr_time
            
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                
                time = max(grid[x][y], curr_time)
                if time < min_times[x][y]:
                    min_times[x][y] = time
                    heapq.heappush(min_heap, (time, x, y))
        


import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        min_times = [[float('inf')] * m for _ in range(n)]
        min_times[0][0] = grid[0][0]
        min_heap = [(grid[0][0], 0, 0)]

        while min_heap:
            curr_time, i, j = heapq.heappop(min_heap)
            if curr_time > min_times[i][j]:
                continue
            
            if (i, j) == (n-1, m-1):
                return curr_time
            
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                
                time = max(grid[x][y], curr_time)
                if time < min_times[x][y]:
                    min_times[x][y] = time
                    heapq.heappush(min_heap, (time, x, y))
        
        
