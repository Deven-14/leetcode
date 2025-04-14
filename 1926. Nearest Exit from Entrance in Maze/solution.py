from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([tuple(entrance)])
        visited = set()
        steps = 0
        ROWS, COLS = len(maze), len(maze[0])
        LAST_ROW, LAST_COL = ROWS - 1, COLS - 1

        while queue:
            curr_level_queue = queue
            next_level_queue = deque()

            while curr_level_queue:
                row, col = curr_level_queue.popleft()
                if (row, col) in visited:
                    continue

                if (row == 0 or col == 0 or row == LAST_ROW or col == LAST_COL) and [row, col] != entrance:
                    return steps
                
                visited.add((row, col))
                if (row - 1) >= 0 and maze[row - 1][col] == '.':
                    next_level_queue.append((row - 1, col))
                if (row + 1) < ROWS and maze[row + 1][col] == '.':
                    next_level_queue.append((row + 1, col))
                if (col - 1) >= 0 and maze[row][col - 1] == '.':
                    next_level_queue.append((row, col - 1))
                if (col + 1) < COLS and maze[row][col + 1] == '.':
                    next_level_queue.append((row, col + 1))
            
            queue = next_level_queue
            steps += 1
        
        return -1


from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([tuple(entrance)])
        visited = set()
        steps = 0
        ROWS, COLS = len(maze), len(maze[0])
        LAST_ROW, LAST_COL = ROWS - 1, COLS - 1

        while queue:
            curr_level_queue = queue
            next_level_queue = deque()

            while curr_level_queue:
                row, col = curr_level_queue.popleft()
                if (row, col) in visited:
                    continue

                if (row == 0 or col == 0 or row == LAST_ROW or col == LAST_COL) and [row, col] != entrance:
                    return steps
                
                visited.add((row, col))

                for next_row, next_col in ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)):
                    if next_row >= 0 and next_row < ROWS and next_col >= 0 and next_col < COLS and maze[next_row][next_col] == "." and (next_row, next_col) not in visited:
                        next_level_queue.append((next_row, next_col))
            
            queue = next_level_queue
            steps += 1
        
        return -1



from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([tuple(entrance)])
        visited = set()
        steps = 0
        ROWS, COLS = len(maze), len(maze[0])
        LAST_ROW, LAST_COL = ROWS - 1, COLS - 1

        while queue:
            curr_level_queue = queue
            next_level_queue = deque()

            while curr_level_queue:
                row, col = curr_level_queue.popleft()
                if (row, col) in visited:
                    continue
                
                if (row == 0 or col == 0 or row == LAST_ROW or col == LAST_COL) and [row, col] != entrance:
                    return steps
                
                visited.add((row, col))
                if row > 0 and maze[row - 1][col] == '.':
                    next_level_queue.append((row - 1, col))
                if row < LAST_ROW and maze[row + 1][col] == '.':
                    next_level_queue.append((row + 1, col))
                if col > 0 and maze[row][col - 1] == '.':
                    next_level_queue.append((row, col - 1))
                if col < LAST_COL and maze[row][col + 1] == '.':
                    next_level_queue.append((row, col + 1))
            
            queue = next_level_queue
            steps += 1
        
        return -1

# * about 60%


from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([tuple(entrance)])
        steps = 0
        ROWS, COLS = len(maze), len(maze[0])
        LAST_ROW, LAST_COL = ROWS - 1, COLS - 1
        maze[entrance[0]][entrance[1]] = '+'

        while queue:
            curr_level_queue = queue
            next_level_queue = deque()

            while curr_level_queue:
                row, col = curr_level_queue.popleft()
                
                if (row == 0 or col == 0 or row == LAST_ROW or col == LAST_COL) and [row, col] != entrance:
                    return steps
                
                if row > 0 and maze[row - 1][col] == '.':
                    next_level_queue.append((row - 1, col))
                    maze[row - 1][col] = '+'
                if row < LAST_ROW and maze[row + 1][col] == '.':
                    next_level_queue.append((row + 1, col))
                    maze[row + 1][col] = '+'
                if col > 0 and maze[row][col - 1] == '.':
                    next_level_queue.append((row, col - 1))
                    maze[row][col - 1] = '+'
                if col < LAST_COL and maze[row][col + 1] == '.':
                    next_level_queue.append((row, col + 1))
                    maze[row][col + 1] = '+'
            
            queue = next_level_queue
            steps += 1
        
        return -1

# * 99.71 %

# * visited for tuple is taking a lot of time.
# * in these scenarios modify the existing grid or create a visited grid