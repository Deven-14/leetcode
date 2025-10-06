class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n_cols = 3
        a_moves = set((i * n_cols) + j for (i, j) in moves[::2])
        b_moves = set((i * n_cols) + j for (i, j) in moves[1::2])
        wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        if any(i in a_moves and j in a_moves and k in a_moves for (i, j, k) in wins):
            return "A"
        if any(i in b_moves and j in b_moves and k in b_moves for (i, j, k) in wins):
            return "B"
        if len(moves) < 9:
            return "Pending"
        return "Draw"