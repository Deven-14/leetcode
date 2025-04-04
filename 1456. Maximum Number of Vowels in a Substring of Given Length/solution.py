class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        window_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                window_vowels += 1
        
        max_vowels = window_vowels

        i, j, n = k, 0, len(s)
        while i < n:
            if s[i] in vowels:
                window_vowels += 1
            if s[j] in vowels:
                window_vowels -= 1
            
            max_vowels = max(max_vowels, window_vowels)
            i += 1
            j += 1
        
        return max_vowels


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        window_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                window_vowels += 1
        
        max_vowels = window_vowels

        i, j, n = k, 0, len(s)
        while i < n:
            if s[i] in vowels:
                window_vowels += 1
            if s[j] in vowels:
                window_vowels -= 1

            if window_vowels > max_vowels:
                max_vowels = window_vowels

            i += 1
            j += 1
        
        return max_vowels