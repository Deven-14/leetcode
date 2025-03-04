class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = sequence.count(word)

        for i in range(n, 0, -1):
            substring = word * i
            if substring in sequence:
                return i
        
        return 0

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        substring = word
        count = 0
        
        while substring in sequence:
            count += 1
            substring += word
        
        return count
