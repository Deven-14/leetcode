from itertools import accumulate
import random
import bisect
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.rect_points = [(abs(x2 - x1) + 1) * (abs(y2 - y1) + 1) for x1, y1, x2, y2 in rects]
        self.acc_rect_points = list(accumulate(self.rect_points))
        self.total_points = self.acc_rect_points[-1]

    def pick(self) -> List[int]:
        selected_point = random.randint(1, self.total_points)
        selected_rect_idx = bisect.bisect_left(self.acc_rect_points, selected_point)
        x1, y1, x2, y2 = self.rects[selected_rect_idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/solutions/316890/trying-to-explain-why-the-intuitive-solution-wont-work



from itertools import accumulate
import random
import bisect
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        rect_points = ((abs(x2 - x1) + 1) * (abs(y2 - y1) + 1) for x1, y1, x2, y2 in rects)
        self.acc_rect_points = list(accumulate(rect_points))
        self.total_points = self.acc_rect_points[-1]

    def pick(self) -> List[int]:
        selected_point = random.randint(1, self.total_points)
        selected_rect_idx = bisect.bisect_left(self.acc_rect_points, selected_point)
        x1, y1, x2, y2 = self.rects[selected_rect_idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/solutions/316890/trying-to-explain-why-the-intuitive-solution-wont-work