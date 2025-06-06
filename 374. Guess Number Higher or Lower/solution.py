# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            num = (l + r) // 2
            res = guess(num)
            if res < 0:
                r = num - 1
            elif res > 0:
                l = num + 1
            else:
                return num


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            num = (l + r) // 2
            res = guess(num)
            match res:
                case 0: return num
                case -1: r = num - 1
                case 1: l = num + 1
        


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            num = (l + r) // 2
            res = guess(num)
            if res == 0:
                return num
            elif res == -1:
                r = num - 1
            else:
                l = num + 1
