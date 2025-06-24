class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        count = 1 if board[0][0] == 'X' else 0

        for i in range(1, m):
            if board[i][0] == 'X' and board[i-1][0] == ".":
                count += 1
        
        for j in range(1, n):
            if board[0][j] == 'X' and board[0][j-1] == ".":
                count += 1
        
        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == 'X' and board[i][j-1] == "." and board[i-1][j] == ".":
                    count += 1
        
        return count