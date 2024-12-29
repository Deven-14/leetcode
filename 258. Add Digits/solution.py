class Solution:
    def addDigits(self, num: int) -> int:
        sum1 = sum(int(n) for n in str(num))
        if sum1 < 10:
            return sum1
        sum1 = str(sum1)
        sum2 = int(sum1[0]) + int(sum1[1])
        if sum2 < 10:
            return sum2
        sum2 = str(sum2)
        sum3 = int(sum2[0]) + int(sum2[1])
        return sum3


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return r if (r := num % 9) else 9
    

# * Also simple idea why digital root equals to mod 9 if we've got an ABCD number
# * ABCD = 1000A+100B+10*C+D = (A + B + C + D) + 9 * (111 * A + 11 * B + C)
# * this equals (mod 9) to A + B + C + D.

# * No iteration explanation though it may be longer.