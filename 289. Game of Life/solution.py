class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        next_states = []
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                i_minus_1, i_plus_1 = i-1, i+1
                j_minus_1, j_plus_1 = j-1, j+1
                live_neighbors = ((board[i_minus_1][j_minus_1] if i_minus_1 >= 0 and j_minus_1 >= 0 else 0)
                + (board[i_minus_1][j] if i_minus_1 >= 0 else 0)
                + (board[i_minus_1][j_plus_1] if i_minus_1 >= 0 and j_plus_1 < m else 0)
                + (board[i][j_minus_1] if j_minus_1 >= 0 else 0)
                + (board[i][j_plus_1] if j_plus_1 < m else 0)
                + (board[i_plus_1][j_minus_1] if i_plus_1 < n and j_minus_1 >= 0 else 0)
                + (board[i_plus_1][j] if i_plus_1 < n else 0)
                + (board[i_plus_1][j_plus_1] if i_plus_1 < n and j_plus_1 < m else 0))
                
                if board[i][j] == 1:
                    if live_neighbors < 2:
                        next_states.append((i, j, 0))
                    elif live_neighbors > 3:
                        next_states.append((i, j, 0))
                
                elif live_neighbors == 3:
                    next_states.append((i, j, 1))
        
        for i, j, next_state in next_states:
            board[i][j] = next_state


# IN PLACE
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        BORN = -1
        DEAD = 0
        ALIVE = 1
        DIED = 2

        def count_live_neighbors(i, j):
            count = 0
            i_minus_1, i_plus_1 = i-1, i+1
            j_minus_1, j_plus_1 = j-1, j+1
            neighbors = (
                (i_minus_1, j_minus_1), (i_minus_1, j), (i_minus_1, j_plus_1),
                (i, j_minus_1), (i, j_plus_1),
                (i_plus_1, j_minus_1), (i_plus_1, j), (i_plus_1, j_plus_1),
            )
            for k, l in neighbors:
                if 0 <= k < n and 0 <= l < m and board[k][l] > 0:
                    count += 1
            
            return count

        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                live_neighbors = count_live_neighbors(i, j)
                
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = DIED
                
                elif live_neighbors == 3:
                    board[i][j] = BORN
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == DIED:
                    board[i][j] = DEAD
                elif board[i][j] == BORN:
                    board[i][j] = ALIVE