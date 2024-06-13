class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_col, end_col, start_row, end_row = 0, len(matrix[0])-1, 0, len(matrix)-1
        result = []

        while start_col < end_col and start_row < end_row:
        
            i = start_col
            while i < end_col:
                result.append(matrix[start_row][i])
                i += 1
            
            i = start_row
            while i < end_row:
                result.append(matrix[i][end_col])
                i += 1
            
            i = end_col
            while i > start_col:
                result.append(matrix[end_row][i])
                i -= 1
            
            i = end_row
            while i > start_row:
                result.append(matrix[i][start_col])
                i -= 1
            
            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1

        if start_row == end_row:
            while start_col <= end_col:
                result.append(matrix[start_row][start_col])
                start_col += 1

        elif start_col == end_col:
            while start_row <= end_row:
                result.append(matrix[start_row][start_col])
                start_row += 1

        return result
