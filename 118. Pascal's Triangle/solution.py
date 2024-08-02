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
            
