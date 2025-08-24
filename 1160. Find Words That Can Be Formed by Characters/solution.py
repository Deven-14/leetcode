from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = 0
        chars = Counter(chars)
        for word in words:
            if Counter(word) <= chars:
                char_count += len(word)
        
        return char_count


from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counts = [0]
        chars = Counter(chars)
        for word in words:
            if Counter(word) <= chars:
                char_counts.append(len(word))
        
        return sum(char_counts)