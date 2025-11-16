from collections import Counter
import string
class Solution:
    def sortString(self, s: str) -> str:
        chars = Counter(s)
        ascending_ascii = string.ascii_lowercase
        descending_ascii = string.ascii_lowercase[::-1]
        result = []

        while chars:
            for char in ascending_ascii:
                if chars[char] > 0:
                    result.append(char)
                    chars[char] -= 1
                else:
                    del chars[char]
            
            for char in descending_ascii:
                if chars[char] > 0:
                    result.append(char)
                    chars[char] -= 1
                else:
                    del chars[char]
        
        return "".join(result)
    


from collections import Counter
import string
class Solution:
    def sortString(self, s: str) -> str:
        chars = Counter(s)
        ascending_ascii = sorted(chars.keys())
        descending_ascii = ascending_ascii[::-1]
        result = []

        while chars:
            for char in ascending_ascii:
                if chars[char] > 0:
                    result.append(char)
                    chars[char] -= 1
                else:
                    del chars[char]
            
            for char in descending_ascii:
                if chars[char] > 0:
                    result.append(char)
                    chars[char] -= 1
                else:
                    del chars[char]
        
        return "".join(result)
    


from collections import Counter
import string
class Solution:
    def sortString(self, s: str) -> str:
        chars = Counter(s)
        n = len(s)
        ascending_ascii = string.ascii_lowercase
        descending_ascii = string.ascii_lowercase[::-1]
        result = []

        while len(result) < n:
            for char in ascending_ascii:
                if chars[char] > 0:
                    result.append(char)
                    chars[char] -= 1
            
            for char in descending_ascii:
                if chars[char] > 0:
                    result.append(char)
                    chars[char] -= 1
        
        return "".join(result)
    


