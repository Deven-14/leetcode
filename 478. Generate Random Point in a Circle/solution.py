from random import random
import math
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.xc = x_center
        self.yc = y_center
        self.pi2 = 2 * math.pi

    def randPoint(self) -> List[float]:
        theta = random() * self.pi2 # [0...1] * (2 * pi)
        r = self.radius * math.sqrt(random()) # random(0, 1)
        return [self.xc + r * math.cos(theta), self.yc + r * math.sin(theta)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

# https://leetcode.com/problems/generate-random-point-in-a-circle/solutions/1113792/generate-random-point-in-a-circle-short-easy-w-explanation-and-diagrams

# https://leetcode.com/problems/generate-random-point-in-a-circle/solutions/1113679/python-polar-coordinates-explained-with-diagrams-and-math

# Rejection Sampling - https://leetcode.com/problems/generate-random-point-in-a-circle/solutions/6655436/master-random-point-generation-inside-a-circle-with-pure-geometry