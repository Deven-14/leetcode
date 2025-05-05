from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        idxs = { char: idx for idx, char in enumerate(s) }
        for char, count in counts.items(): # maintains order, we want the first char with count = 1
            if count == 1:
                return idxs[char]
        
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeating = set()
        seen = set()
        for i, char in enumerate(s):
            if char in seen:
                repeating.add(char)
            else:
                seen.add(char)
        
        for i, char in enumerate(s):
            if char not in repeating:
                return i
        
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, char in enumerate(s):
            if counts[char] == 1:
                return i
        
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for char, count in counts.items(): # maintains order, we want the first char with count = 1
            if count == 1:
                return s.find(char)
        
        return -1
