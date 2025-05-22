import math
class Solution:
    def findComplement(self, num: int) -> int:
        n = int(math.log2(num))+1
        return num ^ ((1 << n)-1)