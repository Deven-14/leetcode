class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click[0], click[1]
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        n, m = len(board), len(board[0])

        def backtrack(i, j, visited):
            visited.add((i, j))
            mines_count = 0
            neighbours = set()

            for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                if x < 0 or x >=n or y < 0 or y >= m or (x, y) in visited:
                    continue
                
                match board[x][y]:
                    case 'M':
                        mines_count += 1
                    case 'E':
                        neighbours.add((x, y))
            
            if mines_count > 0:
                board[i][j] = str(mines_count)
                return
            
            board[i][j] = 'B'
            for x, y in neighbours:
                backtrack(x, y, visited)
        
        backtrack(r, c, set())
        return board


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click[0], click[1]
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        n, m = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def backtrack(i, j, visited):
            visited.add((i, j))
            mines_count = 0
            neighbours = []

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if x < 0 or x >=n or y < 0 or y >= m or (x, y) in visited:
                    continue
                
                match board[x][y]:
                    case 'M':
                        mines_count += 1
                    case 'E':
                        neighbours.append((x, y))
            
            if mines_count > 0:
                board[i][j] = str(mines_count)
                return
            
            board[i][j] = 'B'
            for x, y in neighbours:
                backtrack(x, y, visited)
        
        backtrack(r, c, set())
        return board


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click[0], click[1]
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        n, m = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def backtrack(i, j):
            mines_count = 0
            neighbours = []

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if x < 0 or x >=n or y < 0 or y >= m:
                    continue
                
                match board[x][y]:
                    case 'M':
                        mines_count += 1
                    case 'E':
                        neighbours.append((x, y))
            
            if mines_count > 0:
                board[i][j] = str(mines_count)
                return
            
            board[i][j] = 'B'
            for x, y in neighbours:
                backtrack(x, y)
        
        backtrack(r, c)
        return board



class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click[0], click[1]
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        n, m = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def backtrack(i, j):
            mines_count = 0

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and board[x][y] == 'M':
                    mines_count += 1
            
            if mines_count > 0:
                board[i][j] = str(mines_count)
                return
            
            board[i][j] = 'B'
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and board[x][y] == 'E':
                    backtrack(x, y)
        
        backtrack(r, c)
        return board




class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click[0], click[1]
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        n, m = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def backtrack(i, j):
            mines_count = 0
            neighbours = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
            for x, y in neighbours:
                if 0 <= x < n and 0 <= y < m and board[x][y] == 'M':
                    mines_count += 1
            
            if mines_count > 0:
                board[i][j] = str(mines_count)
                return
            
            board[i][j] = 'B'
            for x, y in neighbours:
                if 0 <= x < n and 0 <= y < m and board[x][y] == 'E':
                    backtrack(x, y)
        
        backtrack(r, c)
        return board


