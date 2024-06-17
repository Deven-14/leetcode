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