class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(''.join('1' if bit == '0' else '0' for bit in f"{n:b}"), 2)