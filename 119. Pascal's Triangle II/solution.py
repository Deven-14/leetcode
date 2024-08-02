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