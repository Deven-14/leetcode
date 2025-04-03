class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        chars = list(s)
        left, right = 0, n-1
        vowels = 'aAeEiIoOuU'

        while left < right:

            while left < right and chars[left] not in vowels:
                left += 1
            
            while right > left and chars[right] not in vowels:
                right -= 1
            
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
            
            left += 1
            right -= 1
        
        return "".join(chars)


class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        chars = list(s)
        left, right = 0, n-1
        vowels = 'aAeEiIoOuU'

        while left < right:

            while left < right and chars[left] not in vowels:
                left += 1
            
            while right > left and chars[right] not in vowels:
                right -= 1
            
            chars[left], chars[right] = chars[right], chars[left]
            
            left += 1
            right -= 1
        
        return "".join(chars)