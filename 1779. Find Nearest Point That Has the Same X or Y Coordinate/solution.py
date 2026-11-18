class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        eles = [(abs(x - x1) + abs(y - y1), idx) for idx, (x1, y1) in enumerate(points) if x1 == x or y1 == y]
        if not eles:
            return -1
        return min(eles)[1]