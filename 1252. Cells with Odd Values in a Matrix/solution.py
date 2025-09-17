class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        odd_rows = [False] * m
        odd_cols = [False] * n

        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True
        
        total_odd_rows = sum(odd_rows)
        total_odd_cols = sum(odd_cols)

        return total_odd_rows * (n - total_odd_cols) + total_odd_cols * (m - total_odd_rows)