class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1) if len(word1) < len(word2) else len(word2)
        combined_word = [""] * (n * 2)
        combined_word[::2] = word1[:n]
        combined_word[1::2] = word2[:n]

        if len(word1) > n:
            combined_word.extend(word1[n:])
        
        if len(word2) > n:
            combined_word.extend(word2[n:])
        
        return "".join(combined_word)



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        combined_word = [""] * (n * 2)
        combined_word[::2] = word1[:n]
        combined_word[1::2] = word2[:n]

        if len(word1) > n:
            combined_word.extend(word1[n:])
        
        if len(word2) > n:
            combined_word.extend(word2[n:])
        
        return "".join(combined_word)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined_word = []
        n = min(len(word1), len(word2))
        for i in range(n):
            combined_word.append(word1[i])
            combined_word.append(word2[i])
        
        if len(word1) > n:
            combined_word.extend(word1[n:])
        
        if len(word2) > n:
            combined_word.extend(word2[n:])
        
        return "".join(combined_word)



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined_word = []
        n = min(len(word1), len(word2))
        for i in range(n):
            combined_word.append(word1[i])
            combined_word.append(word2[i])
        
        combined_word.extend(word1[n:])
        combined_word.extend(word2[n:])
        
        return "".join(combined_word)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        combined_word = [""] * (n * 2)
        combined_word[::2] = word1[:n]
        combined_word[1::2] = word2[:n]

        combined_word.extend(word1[n:])
        combined_word.extend(word2[n:])
        
        return "".join(combined_word)