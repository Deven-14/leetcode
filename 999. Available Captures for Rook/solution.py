class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ROWS, COLS = len(board), len(board[0])

        def check_attacking(i, j):
            attacking = 0
            for up in range(i-1, -1, -1):
                if board[up][j] == 'B':
                    break
                if board[up][j] == 'p':
                    attacking += 1
                    break
            
            for down in range(i+1, ROWS):
                if board[down][j] == 'B':
                    break
                if board[down][j] == 'p':
                    attacking += 1
                    break

            for left in range(j-1, -1, -1):
                if board[i][left] == 'B':
                    break
                if board[i][left] == 'p':
                    attacking += 1
                    break
                
            for right in range(j+1, COLS):
                if board[i][right] == 'B':
                    break
                if board[i][right] == 'p':
                    attacking += 1
                    break
            
            return attacking

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'R':
                    return check_attacking(i, j)
        