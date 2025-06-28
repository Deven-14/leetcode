import string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        n = len(s)

        for char in string.ascii_uppercase:
            start, end = 0, 0
            t = k
            while end < n:
                if s[end] == char:
                    end += 1
                elif t > 0:
                    t -= 1
                    end += 1
                else:
                    while s[start] == char:
                        start += 1
                    start += 1
                    t += 1
                
                longest = max(longest, end - start)
        
        return longest


import string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        n = len(s)

        for char in set(s):
            start, end = 0, 0
            t = k
            while end < n:
                if s[end] == char:
                    end += 1
                elif t > 0:
                    t -= 1
                    end += 1
                else:
                    while s[start] == char:
                        start += 1
                    start += 1
                    t += 1
                
                longest = max(longest, end - start)
        
        return longest


import string
from collections import deque
from itertools import groupby
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k == 0:
            return max(len(list(g)) for k, g in groupby(s))

        longest = 0
        n = len(s)

        for char in set(s):
            start, end = 0, 0
            t = k
            idx = deque()
            while end < n:
                if s[end] == char:
                    end += 1
                elif t > 0:
                    t -= 1
                    end += 1
                    idx.append(end)
                else:
                    start = idx.popleft()
                    t += 1
                
                longest = max(longest, end - start)
        
        return longest


from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        changes = 0
        start = 0
        longest = 0
        char_counts = defaultdict(int)

        for char in s:
            char_counts[char] += 1
            if char_counts[char] > longest:
                longest = char_counts[char]
            elif changes == k:
                char_counts[s[start]] -= 1
                start += 1
            else:
                changes += 1
        
        return longest + changes