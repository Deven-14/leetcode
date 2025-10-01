class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        while k:
            t = min(k, n)
            i, j = 0, m-1

            new_grid = [None] * m
            while i < m:
                curr, prev = grid[i], grid[j]
                curr_partial, prev_partial = curr[:-t], prev[-t:]
                new_row = prev_partial + curr_partial
                new_grid[i] = new_row
                i, j = i + 1, (j + 1) % m

            k -= t
            grid = new_grid
        
        return grid
            


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        new_grid = [[0] * n for _ in range(m)]
        diff = [divmod(t, n) for t in range(k, k + n)]

        for i in range(m):
            for j in range(n):
                add_rows, new_col = diff[j]
                new_j = new_col
                new_i = (i + add_rows) % m
                new_grid[new_i][new_j] = grid[i][j]
        
        return new_grid
    

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nums = [num for row in grid for num in row]
        m, n = len(grid), len(grid[0])
        k %= (m * n)
        
        nums = nums[-k:] + nums[:-k] # shift k times
        new_grid = [nums[i * n : i * n + n] for i in range(m)]
        return new_grid


