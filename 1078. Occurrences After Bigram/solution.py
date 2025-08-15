class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        n = len(words)
        third_words = []

        for i in range(n-2):
            if words[i] == first and words[i+1] == second:
                third_words.append(words[i+2])
        
        return third_words