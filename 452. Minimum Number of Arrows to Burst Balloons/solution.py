class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])

        count = 0
        prev_end = float("-inf")
        for start, end in points:
            if start > prev_end:
                count += 1
                prev_end = end
            
        return count
                