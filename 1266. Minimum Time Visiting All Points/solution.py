class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x1, y1 = points[0]
        min_time = 0

        for i in range(1, len(points)):
            x2, y2 = points[i]
            min_time += max(abs(x2 - x1), abs(y2 - y1))
            x1, y1 = x2, y2
    
        return min_time
