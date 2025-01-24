from itertools import accumulate
class NumArray:

    def __init__(self, nums: List[int]):
        self.running_sum = list(accumulate(nums))
        self.running_sum.append(0)

    def sumRange(self, left: int, right: int) -> int:
        return self.running_sum[right] - self.running_sum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)