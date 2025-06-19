class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)
        last = n-1

        while i < last:
            i += (1 if bits[i] == 0 else 2)
        
        if i == n:
            return False
        
        return True