from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlateCount = Counter(char.lower() for char in licensePlate if char.isalpha())
        shortest_word_len = 16 # based on constraints
        shortest_word = None

        for word in words:
            if Counter(word) >= licensePlateCount and len(word) < shortest_word_len:
                shortest_word = word
                shortest_word_len = len(word)
        
        return shortest_word


from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlateCount = Counter(char.lower() for char in licensePlate if char.isalpha())
        shortest_word_len = 16 # based on constraints
        shortest_word = None

        for word in words:
            if len(word) < shortest_word_len and Counter(word) >= licensePlateCount: # * positioning of conditions makes a lot of difference
                shortest_word = word
                shortest_word_len = len(word)
        
        return shortest_word


from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlateCount = Counter(char for char in licensePlate.lower() if char.isalpha())
        shortest_word_len = 16
        shortest_word = None

        for word in words:
            if len(word) < shortest_word_len and licensePlateCount <= Counter(word): # * positioning of conditions makes a lot of difference
                shortest_word = word
                shortest_word_len = len(word)
        
        return shortest_word
