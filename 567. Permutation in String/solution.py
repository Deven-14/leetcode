from collections import Counter
import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or Counter(s1) > Counter(s2):
            return False
        
        s1_counts = Counter(s1)
        n = len(s1)
        s2_counts = Counter(s2[:n])
        actual = sum(s1_counts[char] == s2_counts[char] for char in string.ascii_lowercase)
        expected = 26 # 26 letters in alphabet

        if actual == expected:
            return True

        for i in range(n, len(s2)):
            new_char = s2[i]
            s2_counts[new_char] += 1
            if s2_counts[new_char] == s1_counts[new_char]:
                actual += 1
            elif (s2_counts[new_char]-1) == s1_counts[new_char]:
                actual -= 1
            
            old_char = s2[i - n]
            s2_counts[old_char] -= 1
            if s2_counts[old_char] == s1_counts[old_char]:
                actual += 1
            elif (s2_counts[old_char]+1) == s1_counts[old_char]:
                actual -= 1
            
            if actual == expected:
                return True

        return False


from collections import Counter
import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = Counter(s1)
        n = len(s1)
        s2_counts = Counter(s2[:n])

        if s1_counts > s2_counts:
            return False

        actual = sum(s1_counts[char] == s2_counts[char] for char in string.ascii_lowercase)
        expected = 26 # 26 letters in alphabet

        if actual == expected:
            return True

        for i in range(n, len(s2)):
            new_char = s2[i]
            s2_counts[new_char] += 1
            if s2_counts[new_char] == s1_counts[new_char]:
                actual += 1
            elif (s2_counts[new_char]-1) == s1_counts[new_char]:
                actual -= 1
            
            old_char = s2[i - n]
            s2_counts[old_char] -= 1
            if s2_counts[old_char] == s1_counts[old_char]:
                actual += 1
            elif (s2_counts[old_char]+1) == s1_counts[old_char]:
                actual -= 1
            
            if actual == expected:
                return True

        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or set(s1) > set(s2):
            return False
        
        n = len(s1)
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        ord_a = ord('a')

        for i in range(n):
            s1_counts[ord(s1[i]) - ord_a] += 1
            s2_counts[ord(s2[i]) - ord_a] += 1

        actual = sum(s1_counts[i] == s2_counts[i] for i in range(26))
        expected = 26 # 26 letters in alphabet

        if actual == expected:
            return True

        for i in range(n, len(s2)):
            new_char = ord(s2[i]) - ord_a
            s2_counts[new_char] += 1
            if s2_counts[new_char] == s1_counts[new_char]:
                actual += 1
            elif (s2_counts[new_char]-1) == s1_counts[new_char]:
                actual -= 1
            
            old_char = ord(s2[i - n]) - ord_a
            s2_counts[old_char] -= 1
            if s2_counts[old_char] == s1_counts[old_char]:
                actual += 1
            elif (s2_counts[old_char]+1) == s1_counts[old_char]:
                actual -= 1
            
            if actual == expected:
                return True

        return False
