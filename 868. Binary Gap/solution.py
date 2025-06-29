class Solution:
    def binaryGap(self, n: int) -> int:
        start = 0
        bin_str = f"{n:b}"
        first = bin_str.find('1')
        start = first + 1
        d = 0
        
        while (last := bin_str.find('1', start)) != -1:
            d = max(d, last - first)
            first = last
            start = first + 1
        
        return d