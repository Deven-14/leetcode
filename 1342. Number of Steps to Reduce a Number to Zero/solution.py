class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            count += 1
            num = num - 1 if num & 1 else num // 2

        return count


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        count = 0
        while num:
            count += 1 + (num & 1) # add 1 if odd
            num >>= 1 # // 2

        return count-1