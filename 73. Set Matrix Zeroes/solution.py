class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        for i, row in enumerate(matrix):
            for j, ele in enumerate(row):
                if ele == 0:
                    rows.add(i)
                    cols.add(j)
        
        m = len(matrix)
        n = len(matrix[0])
        zero_list = [0] * n
        for i in rows:
            matrix[i] = zero_list[:]
        
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0
        