class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted(point[0] for point in points)
        return max(x2 - x1 for x1, x2 in zip(x, x[1:]))
