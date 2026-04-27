from bisect import bisect_left
from random import randint
class Solution:

    def __init__(self, w: List[int]):
        self.running_weight_sum = list(accumulate(w))
        self.total_weight = self.running_weight_sum[-1]

    def pickIndex(self) -> int:
        r = randint(1, self.total_weight)
        return bisect_left(self.running_weight_sum, r)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()