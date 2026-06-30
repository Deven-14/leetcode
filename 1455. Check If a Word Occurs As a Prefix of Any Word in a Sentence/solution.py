class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        index = 1
        for word in sentence.split():
            if word.startswith(searchWord):
                return index
            index += 1
        
        return -1