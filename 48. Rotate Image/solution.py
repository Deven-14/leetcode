class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i = 0
        n = len(matrix)
        half_n = n // 2
        while i < half_n:
            row_top, row_down, column_start, column_stop = 0+i, n-1-i, 0+i, n-1-i
            
            for j in range(column_stop - column_start):
                temp = matrix[row_top][column_start + j]
                matrix[row_top][column_start + j] = matrix[row_down - j][column_start]
                matrix[row_down - j][column_start] = matrix[row_down][column_stop - j]
                matrix[row_down][column_stop - j] = matrix[row_top + j][column_stop]
                matrix[row_top + j][column_stop] = temp
            
            i += 1
