from collections import defaultdict
from random import choice
class Solution:

    def __init__(self, nums: List[int]):
        self.nums_to_index = defaultdict(list)
        for i, num in enumerate(nums):
            self.nums_to_index[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.nums_to_index[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


from collections import defaultdict
from random import choice
class Solution:

    def __init__(self, nums: List[int]):
        nums_to_index = defaultdict(list)
        for i, num in enumerate(nums):
            nums_to_index[num].append(i)
        self.nums_to_index = nums_to_index

    def pick(self, target: int) -> int:
        return choice(self.nums_to_index[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)