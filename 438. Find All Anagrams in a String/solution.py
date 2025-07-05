from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcounts = Counter(p)
        n = len(p)
        indices = [i for i in range(len(s)-n+1) if pcounts == Counter(s[i:i+n])]
        return indices


from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcounts = Counter(p)
        n = len(p)
        indices = []
        scounts = Counter(s[:n])
        if scounts == pcounts:
            indices.append(0)

        for i in range(len(s)-n):
            scounts[s[i]] -= 1
            scounts[s[i+n]] += 1
            if scounts == pcounts:
                indices.append(i+1)
        
        return indices


from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p) or set(s) < set(p):
            return []
        
        pcounts = Counter(p)
        n = len(p)
        indices = []
        scounts = Counter(s[:n])
        expected_char_count = len(pcounts.keys())
        
        char_count = 0
        for char in pcounts.keys():
            if pcounts[char] == scounts[char]:
                char_count += 1
        
        if char_count == expected_char_count:
            indices.append(0)
        
        for i in range(len(s)-n):
            scounts[s[i]] -= 1
            if s[i] in pcounts:
                if scounts[s[i]] + 1 == pcounts[s[i]]:
                    char_count -= 1
                elif scounts[s[i]] == pcounts[s[i]]:
                    char_count += 1

            j = i + n   
            scounts[s[j]] += 1
            if s[j] in pcounts:
                if scounts[s[j]] - 1 == pcounts[s[j]]:
                    char_count -= 1
                elif scounts[s[j]] == pcounts[s[j]]:
                    char_count += 1
            
            if char_count == expected_char_count:
                indices.append(i+1)
        
        return indices


# * 50%

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        pcounts = Counter(p)
        n = len(p)
        indices = []
        scounts = Counter(s[:n])
        expected_char_count = len(pcounts.keys())
        
        char_count = 0
        for char in pcounts.keys():
            if pcounts[char] == scounts[char]:
                char_count += 1
        
        if char_count == expected_char_count:
            indices.append(0)
        
        for i in range(len(s)-n):
            char = s[i]
            scounts[char] -= 1
            if char in pcounts:
                if scounts[char] + 1 == pcounts[char]:
                    char_count -= 1
                elif scounts[char] == pcounts[char]:
                    char_count += 1

            char = s[i + n]
            scounts[char] += 1
            if char in pcounts:
                if scounts[char] - 1 == pcounts[char]:
                    char_count -= 1
                elif scounts[char] == pcounts[char]:
                    char_count += 1
            
            if char_count == expected_char_count:
                indices.append(i+1)
        
        return indices

# * 90%

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        pcounts = [0] * 26
        scounts = [0] * 26
        a = ord('a')
        n = len(p)

        for i in range(n):
            pcounts[ord(p[i]) - a] += 1
            scounts[ord(s[i]) - a] += 1

        indices = []
        expected_matches = 26
        matches = sum(1 for i in range(26) if scounts[i] == pcounts[i])
        
        if matches == expected_matches:
            indices.append(0)
        
        for i in range(len(s)-n):
            char = ord(s[i]) - a
            scounts[char] -= 1
            if scounts[char] + 1 == pcounts[char]:
                matches -= 1
            elif scounts[char] == pcounts[char]:
                matches += 1

            char = ord(s[i + n]) - a
            scounts[char] += 1
            if scounts[char] - 1 == pcounts[char]:
                matches -= 1
            elif scounts[char] == pcounts[char]:
                matches += 1
            
            if matches == expected_matches:
                indices.append(i+1)
        
        return indices