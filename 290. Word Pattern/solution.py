class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        key_bijections = {}
        word_bijections = {}
        
        if len(pattern) != len(words):
            return False

        for key, word in zip(pattern, words):
            if key in key_bijections:
                if word != key_bijections[key]:
                    return False
            if word in word_bijections:
                if key != word_bijections[word]:
                    return False
            key_bijections[key] = word
            word_bijections[word] = key
        
        return True