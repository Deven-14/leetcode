class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)[2:]
        ones = set(bin_n[::2])
        zeros = set(bin_n[1::2])
        return ones == {'1'} and (zeros == {'0'} if zeros else True)
    
# * or the general way of bin_n[i] == bin_n[i-1] return False