class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start, stop = 0, m-1
        while start <= stop:
            mid = (start + stop) // 2

            ele = matrix[mid][0]
            if ele == target:
                break
            elif ele > target:
                stop = mid-1
            else:
                start = mid+1
        
        if matrix[mid][0] <= target:
            row = matrix[mid]
        elif matrix[mid][0] > target and mid > 0:
            row = matrix[mid-1]
        else:
            return False

        start, stop = 0, n-1
        while start <= stop:
            mid = (start + stop) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                stop = mid-1
            else:
                start = mid+1
        
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search():
            left, right = 0, len(matrix[0]) - 1
            top, down = 0, len(matrix) - 1

            while left <= right and top <= down:
                l_r_mid = (left + right) // 2 # left + (right - left) // 2
                t_d_mid = (top + down) // 2

                if matrix[t_d_mid][right] < target:
                    top = t_d_mid + 1
                elif matrix[t_d_mid][left] > target:
                    down = t_d_mid - 1
                elif matrix[t_d_mid][l_r_mid] < target: # in middle row
                    left = l_r_mid + 1
                elif matrix[t_d_mid][l_r_mid] > target:
                    right = l_r_mid - 1
                else:
                    return True
            
            return False
        
        return binary_search()


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search():
            left, right = 0, len(matrix[0]) - 1
            top, down = 0, len(matrix) - 1

            while top <= down:
                mid = (top + down) // 2
                if matrix[mid][right] < target:
                    top = mid + 1
                elif matrix[mid][left] > target:
                    down = mid - 1
                else:
                    break # in middle row
            
            if not top <= down:
                return False
            
            row = mid
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] < target: 
                    left = mid + 1
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    return True
            
            return False
        
        return binary_search()