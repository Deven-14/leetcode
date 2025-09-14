class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # y = mx + c - straight line equation
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if (x2 - x1) == 0:
            k = x1 # x = k is equation when m = infinity
            return all(x == k for x, _ in coordinates)

        elif (y2 - y1) == 0:
            k = y1 # y = k is equation when m = 0
            return all(y == k for _, y in coordinates)
        
        m = (y2 - y1) / (x2 - x1)
        c = y1 - (m * x1)
        return all(y == m * x + c for x, y in coordinates)