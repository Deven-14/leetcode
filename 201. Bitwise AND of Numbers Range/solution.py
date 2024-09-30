class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left_bin = f"{left:31b}"
        right_bin = f"{right:31b}"

        i = 0
        n = len(left_bin)

        while i < n and left_bin[i] == right_bin[i]:
            i += 1
        
        return int(left_bin[:i] + "0" * (n-i), 2)

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        c = 0
        while left != right:
            left >>= 1
            right >>= 1
            c += 1
        
        return left << c