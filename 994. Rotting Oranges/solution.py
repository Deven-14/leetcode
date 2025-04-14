from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        minutes = -1
        ROWS, COLS = len(grid), len(grid[0])
        LAST_ROW, LAST_COL = ROWS - 1, COLS - 1
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))

        while queue:
            curr_level_queue = queue
            next_level_queue = deque()

            while curr_level_queue:
                row, col = curr_level_queue.popleft()
                
                if row > 0 and grid[row - 1][col] == 1:
                    next_level_queue.append((row - 1, col))
                    grid[row - 1][col] = 2
                if row < LAST_ROW and grid[row + 1][col] == 1:
                    next_level_queue.append((row + 1, col))
                    grid[row + 1][col] = 2
                if col > 0 and grid[row][col - 1] == 1:
                    next_level_queue.append((row, col - 1))
                    grid[row][col - 1] = 2
                if col < LAST_COL and grid[row][col + 1] == 1:
                    next_level_queue.append((row, col + 1))
                    grid[row][col + 1] = 2
            
            queue = next_level_queue
            minutes += 1
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        
        return minutes if minutes > -1 else 0