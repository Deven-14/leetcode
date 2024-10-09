class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping1 = {}
        mapping2 = {}

        for char1, char2 in zip(s, t):
            if char1 not in mapping1:
                mapping1[char1] = char2
            elif mapping1[char1] != char2:
                return False

            if char2 not in mapping2:
                mapping2[char2] = char1
            elif mapping2[char2] != char1:
                return False
        
        return True
    

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        t_chars = set()

        for char1, char2 in zip(s, t):
            if char1 not in mapping:
                if char2 in t_chars:
                    return False
                mapping[char1] = char2
                t_chars.add(char2)
            elif mapping[char1] != char2:
                return False
        
        return True