class Solution:
    def solve_n_queens(self, n: int, i = 0):
        if i == n:
            self.solutions += 2
            if n % 2 != 0 and self.board[0][n//2]:
                self.solutions -= 1
            return
        
        if i == 0:
            num = self.half_n
        else:
            num = n

        mid_dig_index = n-1
        for j in range(num):
            if self.col_has_Q[j] or self.r_dig_has_Q[i+j] or self.l_dig_has_Q[mid_dig_index+i-j]:
                continue
            self.board[i][j] = True
            self.row_has_Q[i] = self.col_has_Q[j] = self.r_dig_has_Q[i+j] = self.l_dig_has_Q[mid_dig_index+i-j] = True
            self.solve_n_queens(n, i+1)
            self.row_has_Q[i] = self.col_has_Q[j] = self.r_dig_has_Q[i+j] = self.l_dig_has_Q[mid_dig_index+i-j] = False
            self.board[i][j] = False

    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        if n <= 3:
            return 0

        if n % 2 == 0:
            self.half_n = n // 2
        else:
            self.half_n = n // 2 + 1
        
        self.solutions = 0
        self.board = [[False] * n for _ in range(n)]

        self.row_has_Q = [False] * n
        self.col_has_Q = [False] * n
        self.r_dig_has_Q = [False] * (2 * n - 1)
        self.l_dig_has_Q = [False] * (2 * n - 1)

        self.solve_n_queens(n)
                
        return self.solutions