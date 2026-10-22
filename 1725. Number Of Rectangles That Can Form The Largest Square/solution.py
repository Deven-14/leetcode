class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        count = 0
        for l, w in rectangles:
            min_len = min(l, w)
            if min_len > max_len:
                max_len = min_len
                count = 1
            elif min_len == max_len:
                count += 1
        
        return count


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        square_sides = [min(l, w) for l, w in rectangles]
        return square_sides.count(max(square_sides))

