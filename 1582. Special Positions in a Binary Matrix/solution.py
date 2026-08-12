class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        row = [0] * n
        col = [0] * m

        for i in range(n):
            for j in range(m):
                row[i] += mat[i][j]
                col[j] += mat[i][j]
        
        rows_with_1 = [i for i in range(n) if row[i] == 1]
        cols_with_1 = [j for j in range(m) if col[j] == 1]

        count = 0
        for i in rows_with_1:
            for j in cols_with_1:
                if mat[i][j] == 1:
                    count += 1
        
        return count


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        row = [sum(r) for r in mat]
        col = [sum(c) for c in zip(*mat)]
        
        rows_with_1 = [i for i in range(n) if row[i] == 1]
        cols_with_1 = [j for j in range(m) if col[j] == 1]

        count = sum(
            1 for i in rows_with_1
            for j in cols_with_1
            if mat[i][j] == 1
        )

        return count

