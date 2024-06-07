from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        RLE = self.countAndSay(n-1)
        new_RLE = []
        for k, g in groupby(RLE):
            n = len(list(g))
            new_RLE.append(f"{n}{k}")
        
        return "".join(new_RLE)