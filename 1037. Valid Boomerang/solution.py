class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) != 0


# It's a basic high school geometry problem.
# What question is asking to return if all three points can be joined by a single straight line ( i.e we have to return if the given three points are non-collinear)

# So if three points are non collinear then they form triangle. So all we need to check if the area of the triangle formed is non-zero. If the area is zero it means all three points are collinear.

# Suppose the three points are (x1,y1), (x2,y2), (x3,y3).
# So area of triangle is given by : 0.5 * [x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)]

# Thus we just need to check the condition if [x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)] !=0