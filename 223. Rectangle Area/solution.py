class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def calculate_distance(x1, x2):
            if x1 >= 0 and x2 >= 0:
                return abs(x1-x2)
            elif x1 >= 0 and x2 < 0:
                return x1-x2
            elif x1 < 0 and x2 >= 0:
                return x2-x1
            else:
                return abs(x1-x2)
        
        l1, w1 = calculate_distance(ax1, ax2), calculate_distance(ay1, ay2)
        l2, w2 = calculate_distance(bx1, bx2), calculate_distance(by1, by2)

        if bx1 >= ax2 or ax1 >= bx2 or by1 >= ay2 or ay1 >= by2:
            return l1*w1 + l2*w2

        cx1, cx2 = max(ax1, bx1), min(ax2, bx2)
        cy1, cy2 = max(ay1, by1), min(ay2, by2)
        overlapping_area = max(0, cx2 - cx1) * max(0, cy2 - cy1)

        return  l1*w1 + l2*w2 - overlapping_area
