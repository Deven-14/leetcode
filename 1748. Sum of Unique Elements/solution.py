class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        return sum(num for num, count in Counter(nums).items() if count == 1)