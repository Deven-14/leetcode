class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i] + mat[i][-i-1]
        
        if n % 2 == 1:
            mid = n // 2
            total -= mat[mid][mid]
        
        return total