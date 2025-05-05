from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tcount = Counter(t)
        scount = Counter(s)
        for char in tcount:
            if tcount[char] > scount[char]:
                return char

from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0

        for char in s + t:
            res ^= ord(char)
        
        return chr(res)
