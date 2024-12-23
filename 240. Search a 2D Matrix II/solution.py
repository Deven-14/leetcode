class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row_start, col_start = 0, 0
        row_end, col_end = n-1, m-1

        while row_start <= row_end and col_start <= col_end:
            i, j = col_start, col_end
            while i <= j:
                mid = (i + j) // 2
                num = matrix[row_start][mid]
                if num == target:
                    break
                elif num > target:
                    j = mid-1
                else:
                    i = mid+1
            
            if num == target:
                return True
            elif num > target:
                col_end = mid-1
            else:
                col_end = mid
            
            i, j = row_start, row_end
            while i <= j:
                mid = (i + j) // 2
                num = matrix[mid][col_start]
                if num == target:
                    break
                elif num > target:
                    j = mid-1
                else:
                    i = mid+1
            
            if num == target:
                return True
            elif num > target:
                row_end = mid-1
            else:
                row_end = mid
            
            row_start += 1
            col_start += 1

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row_start, col_start = 0, 0
        row_end, col_end = n-1, m-1

        while row_start <= row_end and col_start <= col_end:
            i, j = col_start, col_end
            while i <= j:
                mid = (i + j) // 2
                num = matrix[row_start][mid]
                if num == target:
                    return True
                elif num > target:
                    j = mid-1
                else:
                    i = mid+1
            
            if num > target:
                col_end = mid-1
            else:
                col_end = mid
            
            i, j = row_start, row_end
            while i <= j:
                mid = (i + j) // 2
                num = matrix[mid][col_start]
                if num == target:
                    return  True
                elif num > target:
                    j = mid-1
                else:
                    i = mid+1
            
            if num > target:
                row_end = mid-1
            else:
                row_end = mid
            
            row_start += 1
            col_start += 1

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row, col = 0, m-1
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False