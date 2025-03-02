from itertools import pairwise
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = [1]
        for i in range(rowIndex):
            row = [1]
            for num1, num2 in pairwise(prev_row):
                row.append(num1+num2)
            row.append(1)
            prev_row = row

        return prev_row

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev_row = [1, 1]
        for _ in range(2, rowIndex+1):
            row = [1]
            row.extend(num1 + num2 for num1, num2 in pairwise(prev_row))
            row.append(1)
            prev_row = row
        
        return prev_row