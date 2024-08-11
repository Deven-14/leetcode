class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        n_1, m_1 = n-1, m-1
        non_capturable = [[False] * m for _ in range(n)]

        def mark_non_capturable(i, j):
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                non_capturable[a][b] = True
                if b-1 > 0 and not non_capturable[a][b-1] and board[a][b-1] == "O":
                    stack.append((a, b-1))
                if b+1 < m and not non_capturable[a][b+1] and board[a][b+1] == "O":
                    stack.append((a, b+1))
                if a-1 > 0 and not non_capturable[a-1][b] and board[a-1][b] == "O":
                    stack.append((a-1, b))
                if a+1 < n and not non_capturable[a+1][b] and board[a+1][b] == "O":
                    stack.append((a+1, b))

        for i in range(n):
            if board[i][0] == "O":
                mark_non_capturable(i, 0)
            if board[i][m_1] == "O":
                mark_non_capturable(i, m_1)
        
        for j in range(m):
            if board[0][j] == "O":
                mark_non_capturable(0, j)
            if board[n_1][j] == "O":
                mark_non_capturable(n_1, j)

        def capture(i, j):
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                board[a][b] = "X"
                if not non_capturable[a][b-1] and board[a][b-1] == "O":
                    stack.append((a, b-1))
                if not non_capturable[a][b+1] and board[a][b+1] == "O":
                    stack.append((a, b+1))
                if not non_capturable[a-1][b] and board[a-1][b] == "O":
                    stack.append((a-1, b))
                if not non_capturable[a+1][b] and board[a+1][b] == "O":
                    stack.append((a+1, b))

        for i in range(1, n-1):
            for j in range(1, m-1):
                if board[i][j] == "O" and not non_capturable[i][j] and (board[i][j-1] == "X" or board[i][j+1] == "X" or board[i-1][j] == "X" or board[i+1][j] == "X"):
                    capture(i, j)
        

        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        n_1, m_1 = n-1, m-1

        def mark_non_capturable(i, j):
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                board[a][b] = "Y"
                if b-1 > 0 and board[a][b-1] == "O":
                    stack.append((a, b-1))
                if b+1 < m and board[a][b+1] == "O":
                    stack.append((a, b+1))
                if a-1 > 0 and board[a-1][b] == "O":
                    stack.append((a-1, b))
                if a+1 < n and board[a+1][b] == "O":
                    stack.append((a+1, b))

        for i in range(n):
            if board[i][0] == "O":
                mark_non_capturable(i, 0)
            if board[i][m_1] == "O":
                mark_non_capturable(i, m_1)
        
        for j in range(m):
            if board[0][j] == "O":
                mark_non_capturable(0, j)
            if board[n_1][j] == "O":
                mark_non_capturable(n_1, j)

        def capture(i, j):
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                board[a][b] = "X"
                if board[a][b-1] == "O":
                    stack.append((a, b-1))
                if board[a][b+1] == "O":
                    stack.append((a, b+1))
                if board[a-1][b] == "O":
                    stack.append((a-1, b))
                if board[a+1][b] == "O":
                    stack.append((a+1, b))

        for i in range(1, n-1):
            for j in range(1, m-1):
                if board[i][j] == "O" and (board[i][j-1] == "X" or board[i][j+1] == "X" or board[i-1][j] == "X" or board[i+1][j] == "X"):
                    capture(i, j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "Y":
                    board[i][j] = "O"
        

        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        n_1, m_1 = n-1, m-1

        def mark_non_capturable(i, j):
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                board[a][b] = "Y"
                if b-1 > 0 and board[a][b-1] == "O":
                    stack.append((a, b-1))
                if b+1 < m and board[a][b+1] == "O":
                    stack.append((a, b+1))
                if a-1 > 0 and board[a-1][b] == "O":
                    stack.append((a-1, b))
                if a+1 < n and board[a+1][b] == "O":
                    stack.append((a+1, b))

        for i in range(n):
            if board[i][0] == "O":
                mark_non_capturable(i, 0)
            if board[i][m_1] == "O":
                mark_non_capturable(i, m_1)
        
        for j in range(m):
            if board[0][j] == "O":
                mark_non_capturable(0, j)
            if board[n_1][j] == "O":
                mark_non_capturable(n_1, j)

        for i in range(1, n-1):
            for j in range(1, m-1):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "Y":
                    board[i][j] = "O"
        

        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        n_1, m_1 = n-1, m-1

        def mark_non_capturable(i, j):
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                board[a][b] = "Y"
                if b-1 > 0 and board[a][b-1] == "O":
                    stack.append((a, b-1))
                if b+1 < m and board[a][b+1] == "O":
                    stack.append((a, b+1))
                if a-1 > 0 and board[a-1][b] == "O":
                    stack.append((a-1, b))
                if a+1 < n and board[a+1][b] == "O":
                    stack.append((a+1, b))

        for i in range(n):
            if board[i][0] == "O":
                mark_non_capturable(i, 0)
            if board[i][m_1] == "O":
                mark_non_capturable(i, m_1)
        
        for j in range(m):
            if board[0][j] == "O":
                mark_non_capturable(0, j)
            if board[n_1][j] == "O":
                mark_non_capturable(n_1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "Y":
                    board[i][j] = "O"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        n_1, m_1 = n-1, m-1

        def mark_non_capturable(i, j):
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                board[a][b] = "Y"
                if (c := b-1) > 0 and board[a][c] == "O":
                    stack.append((a, c))
                if (c := b+1) < m and board[a][c] == "O":
                    stack.append((a, c))
                if (c := a-1) > 0 and board[c][b] == "O":
                    stack.append((c, b))
                if (c := a+1) < n and board[c][b] == "O":
                    stack.append((c, b))

        for i in range(n):
            if board[i][0] == "O":
                mark_non_capturable(i, 0)
            if board[i][m_1] == "O":
                mark_non_capturable(i, m_1)
        
        for j in range(m):
            if board[0][j] == "O":
                mark_non_capturable(0, j)
            if board[n_1][j] == "O":
                mark_non_capturable(n_1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "Y":
                    board[i][j] = "O"
        