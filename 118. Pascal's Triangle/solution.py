from itertools import pairwise
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows =[[1]]
        for i in range(1, numRows):
            prev_row = rows[i-1]
            row = [1]
            for num1, num2 in pairwise(prev_row):
                row.append(num1+num2)
            row.append(1)
            rows.append(row)
        
        return rows
            
from itertools import pairwise
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        rows = [[1], [1, 1]]
        prev_row = rows[-1]
        row = [1]
        for _ in range(3, numRows+1):
            row = [1]
            row.extend(num1 + num2 for num1, num2 in pairwise(prev_row))
            row.append(1)
            rows.append(row)
            prev_row = row
        
        return rows
