from copy import deepcopy

class Solution:
    def does_attack(self, n, board, i, j) -> bool:
        for k in range(0, i):
            if board[k][j]:
                return True
            left = j-i+k
            if left >= 0 and board[k][left]:
                return True
            right = j+i-k
            if right < n and board[k][right]:
                return True
        return False
    

    def solve_n_queens(self, n: int, solutions, board, i = 0):
        if i == n:
            solutions.append(deepcopy(board)) # be careful
            return
        
        for j in range(n):
            if self.does_attack(n, board, i , j):
                continue
            board[i][j] = True
            self.solve_n_queens(n, solutions, board, i+1)
            board[i][j] = False
    
    def convert_solutions_to_Q(self, solutions):
        outputs = []
        for solution in solutions:
            output = []
            for row in solution:
                row_output = []
                for col in row:
                    row_output.append("." if not col else "Q")
                output.append("".join(row_output))
            outputs.append(output)
        
        return outputs
                    
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        board = [[False] * n for _ in range(n)]
        self.solve_n_queens(n, solutions, board)
        return self.convert_solutions_to_Q(solutions)


from copy import deepcopy

class Solution:
    def does_attack(self, n, board, i, j) -> bool:
        for k in range(0, i):
            if board[k][j] == "Q":
                return True
            left = j-i+k
            if left >= 0 and board[k][left] == "Q":
                return True
            right = j+i-k
            if right < n and board[k][right] == "Q":
                return True
        return False
    

    def solve_n_queens(self, n: int, solutions, board, i = 0):
        if i == n:
            solutions.append(["".join(row) for row in board])
            return
        
        for j in range(n):
            if self.does_attack(n, board, i , j):
                continue
            board[i][j] = "Q"
            self.solve_n_queens(n, solutions, board, i+1)
            board[i][j] = "."
                    
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        board = [["."] * n for _ in range(n)]
        self.solve_n_queens(n, solutions, board)
        return solutions



from copy import deepcopy

class Solution:
    def does_attack(self, n, board, i, j) -> bool:
        for k in range(0, i):
            if board[k][j] == "Q":
                return True
            left = j-i+k
            if left >= 0 and board[k][left] == "Q":
                return True
            right = j+i-k
            if right < n and board[k][right] == "Q":
                return True
        return False
    

    def solve_n_queens(self, n: int, solutions, board, i = 0):
        if i == n:
            solutions.append(["".join(row) for row in board])
            return
        
        for j in range(n):
            if i == 0:
                if n % 2 == 0 and j > (n//2 - 1):
                    break
                elif j > (n//2):
                    break
            if self.does_attack(n, board, i , j):
                continue
            board[i][j] = "Q"
            self.solve_n_queens(n, solutions, board, i+1)
            board[i][j] = "."
                    
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        solutions = []
        board = [["."] * n for _ in range(n)]
        self.solve_n_queens(n, solutions, board)
        
        # reversing solutions
        remaining_solutions = []
        for solution in solutions:
            if n % 2 != 0 and solution[0][n // 2] == "Q":
                continue
            remaining_solutions.append([row[::-1] for row in solution])

        all_solutions = solutions + remaining_solutions[::-1]    
        
        return all_solutions


from copy import deepcopy

class Solution:
    def does_attack(self, n, board, i, j) -> bool:
        for k in range(0, i):
            if board[k][j] == "Q":
                return True
            left = j-i+k
            if left >= 0 and board[k][left] == "Q":
                return True
            right = j+i-k
            if right < n and board[k][right] == "Q":
                return True
        return False
    

    def solve_n_queens(self, n: int, solutions, board, i = 0):
        if i == n:
            solutions.append(["".join(row) for row in board])
            return
        
        if i == 0:
            if n % 2 == 0:
                num = n // 2
            else:
                num = n // 2 + 1
        else:
            num = n

        for j in range(num):
            if self.does_attack(n, board, i , j):
                continue
            board[i][j] = "Q"
            self.solve_n_queens(n, solutions, board, i+1)
            board[i][j] = "."
                    
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        solutions = []
        board = [["."] * n for _ in range(n)]
        self.solve_n_queens(n, solutions, board)
        
        # reversing solutions
        remaining_solutions = []
        for solution in solutions:
            if n % 2 != 0 and solution[0][n // 2] == "Q":
                continue
            remaining_solutions.append([row[::-1] for row in solution])

        all_solutions = solutions + remaining_solutions[::-1]    
        
        return all_solutions


class Solution:
    def does_attack(self, n, board, i, j) -> bool:
        left, right = j-i, j+i
        for k in range(0, i):
            if board[k][j] == "Q":
                return True
            l = left+k
            if l >= 0 and board[k][l] == "Q":
                return True
            r = right-k
            if r < n and board[k][r] == "Q":
                return True
        return False
    

    def solve_n_queens(self, n: int, solutions, board, i = 0):
        if i == n:
            solutions.append(["".join(row) for row in board])
            return
        
        if i == 0:
            if n % 2 == 0:
                num = n // 2
            else:
                num = n // 2 + 1
        else:
            num = n

        for j in range(num):
            if self.does_attack(n, board, i , j):
                continue
            board[i][j] = "Q"
            self.solve_n_queens(n, solutions, board, i+1)
            board[i][j] = "."
                    
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n == 3:
            return []
        solutions = []
        board = [["."] * n for _ in range(n)]
        self.solve_n_queens(n, solutions, board)
        
        # reversing solutions
        remaining_solutions = []
        for solution in solutions:
            if n % 2 != 0 and solution[0][n // 2] == "Q":
                continue
            remaining_solutions.append([row[::-1] for row in solution])

        all_solutions = solutions + remaining_solutions[::-1]    
        
        return all_solutions


class Solution:
    def solve_n_queens(self, n: int, i = 0):
        if i == n:
            self.solutions.append(["".join(row) for row in self.board])
            return
        
        if i == 0:
            num = self.half_n
        else:
            num = n

        mid_dig_index = n-1
        for j in range(num):
            if self.col_has_Q[j] or self.r_dig_has_Q[i+j] or self.l_dig_has_Q[mid_dig_index+i-j]:
                continue
            self.board[i][j] = "Q"
            self.row_has_Q[i] = self.col_has_Q[j] = self.r_dig_has_Q[i+j] = self.l_dig_has_Q[mid_dig_index+i-j] = True
            self.solve_n_queens(n, i+1)
            self.row_has_Q[i] = self.col_has_Q[j] = self.r_dig_has_Q[i+j] = self.l_dig_has_Q[mid_dig_index+i-j] = False
            self.board[i][j] = "."
                    
    def get_remaining_reversed_solutions(self, n):
        remaining_solutions = []
        for solution in self.solutions:
            if n % 2 != 0 and solution[0][n // 2] == "Q":
                continue
            remaining_solutions.append([row[::-1] for row in solution])
        
        return remaining_solutions
    

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n <= 3:
            return []

        if n % 2 == 0:
            self.half_n = n // 2
        else:
            self.half_n = n // 2 + 1
        
        self.solutions = []
        self.board = [["."] * n for _ in range(n)]

        self.row_has_Q = [False] * n
        self.col_has_Q = [False] * n
        self.r_dig_has_Q = [False] * (2 * n - 1)
        self.l_dig_has_Q = [False] * (2 * n - 1)

        self.solve_n_queens(n)
        
        remaining_solutions = self.get_remaining_reversed_solutions(n)

        all_solutions = self.solutions + remaining_solutions[::-1]    
        
        return all_solutions
