class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy_area = sum(sum(1 for x in row if x != 0) for row in grid)
        xz_area = sum(max(row) for row in grid)
        yz_area = sum(max(row) for row in zip(*grid))
        return xy_area + xz_area + yz_area


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy_area = sum(1 for row in grid for ele in row if ele != 0)
        xz_area = sum(max(row) for row in grid)
        yz_area = sum(max(row) for row in zip(*grid))
        return xy_area + xz_area + yz_area