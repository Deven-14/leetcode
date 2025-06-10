from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums[:]
        self.last = len(nums)-1

    def reset(self) -> List[int]:
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        # Fisher-Yates algorithm 
        arr = self.nums
        for i in range(self.last, 0, -1):
            j = randint(0, i) # randrange [0, i), for randint [0, i]
            arr[i], arr[j] = arr[j], arr[i]

        return arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()



from random import shuffle
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

