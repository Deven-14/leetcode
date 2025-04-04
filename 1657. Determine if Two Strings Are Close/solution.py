from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        counts1 = Counter(word1)
        counts2 = Counter(word2)
        return counts1.keys() == counts2.keys() and Counter(counts1.values()) == Counter(counts2.values())


from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        if set(word1) != set(word2):
            return False
        
        counts1 = Counter(word1)
        counts2 = Counter(word2)
        return Counter(counts1.values()) == Counter(counts2.values())
        