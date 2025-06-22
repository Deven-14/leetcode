class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            if matrix[i-1][:-1] != matrix[i][1:]:
                return False
        
        return True


# range m
#   range n
#      if [i][j] != [i-1][j-1]: return False
