class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda word: len(word), reverse=True)

        substrings = []
        for i in range(1, len(words)):
            for j in range(i-1, -1, -1):
                if words[i] in words[j]:
                    substrings.append(words[i])
                    break
        
        return substrings