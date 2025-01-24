from itertools import accumulate
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        col_running_sums = [list(accumulate(col)) for col in zip(*matrix)]
        self.running_sums = [list(accumulate(row)) for row in zip(*col_running_sums)]
        for running_sum in self.running_sums:
            running_sum.append(0)
        self.running_sums.append([0] * len(self.running_sums[0]))
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.running_sums[row2][col2] - self.running_sums[row1-1][col2] - self.running_sums[row2][col1-1] + self.running_sums[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)