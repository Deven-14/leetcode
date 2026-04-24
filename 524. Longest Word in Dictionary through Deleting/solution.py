class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda word: (-len(word), word))
        for word in dictionary:
            it = iter(s)
            if all(c in it for c in word):
                return word
        
        return ""