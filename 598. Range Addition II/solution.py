class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n
        min_row, min_col = min(x[0] for x in ops), min(x[1] for x in ops)
        return min_row * min_col