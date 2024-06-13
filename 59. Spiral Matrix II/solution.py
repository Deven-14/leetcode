class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        start_col, end_col, start_row, end_row = 0, n-1, 0, n-1
        matrix = [[0] * n for _ in range(n)]
        count = 1

        while start_col < end_col and start_row < end_row:
        
            i = start_col
            while i < end_col:
                matrix[start_row][i] = count
                count += 1
                i += 1
            
            i = start_row
            while i < end_row:
                matrix[i][end_col] = count
                count += 1
                i += 1
            
            i = end_col
            while i > start_col:
                matrix[end_row][i] = count
                count += 1
                i -= 1
            
            i = end_row
            while i > start_row:
                matrix[i][start_col] = count
                count += 1
                i -= 1
            
            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1

        if start_row == end_row:
            while start_col <= end_col:
                matrix[start_row][start_col] = count
                count += 1
                start_col += 1

        elif start_col == end_col:
            while start_row <= end_row:
                matrix[start_row][start_col] = count
                count += 1
                start_row += 1

        return matrix


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        start_col, end_col, start_row, end_row = 0, n-1, 0, n-1
        matrix = [[0] * n for _ in range(n)]
        count = 1

        while start_col < end_col and start_row < end_row:
        
            end = count + (end_col - start_col)
            matrix[start_row][start_col:end_col] = range(count, end)
            count = end
            
            i = start_row
            while i < end_row:
                matrix[i][end_col] = count
                count += 1
                i += 1
            
            end = count + (end_col - start_col)
            matrix[end_row][end_col:start_col:-1] = range(count, end)
            count = end

            i = end_row
            while i > start_row:
                matrix[i][start_col] = count
                count += 1
                i -= 1
            
            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1

        if start_row == end_row:
            end = count + (end_col - start_col) + 1
            matrix[start_row][start_col:end_col+1] = range(count, end)
            count = end

        elif start_col == end_col:
            while start_row <= end_row:
                matrix[start_row][start_col] = count
                count += 1
                start_row += 1

        return matrix
