class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        @cache
        def dist(p1, p2): 
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        @cache
        def are_perpendicular(p1, p2, p3):
            return (p1[0] - p2[0]) * (p3[0] - p2[0]) + (p1[1] - p2[1]) * (p3[1] - p2[1]) == 0

        for x1, x2, x3, x4 in permutations([tuple(p1), tuple(p2), tuple(p3), tuple(p4)]):
            if dist(x1, x2) == dist(x2, x3) == dist(x3, x4) == dist(x4, x1) > 0 and are_perpendicular(x1, x2, x3) and are_perpendicular(x2, x3, x4) and are_perpendicular(x3, x4, x1) and are_perpendicular(x4, x1, x2):
                return True
        
        return False


# (x1, y1), (x2, y2), (x3, y3) 3 points
# (x2, y2) is the intersecting point, I want to check if the intersecting angle is 90 degress

# m1 * m2 = -1 for perpendicular lines
# if you expand it then
# (x1-x2)(x3-x2)+(y1-y2)(y3-y2)=0



class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dist = lambda p1, p2: (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        d = sorted([
            dist(p1, p2), dist(p1, p3), dist(p1, p4),
            dist(p2, p3), dist(p2, p4), dist(p3, p4)
        ])

        return d[0] == d[1] == d[2] == d[3] > 0 and d[4] == d[5] == 2 * d[0]

# length of diagonal of square = sqrt(2) * sqrt_d
# but we didn't sqrt the d, so both side it's squared
# l^2 = 2 * d

