class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")

        words_in_rows = []
        for word in words:
            word_set = set(word)
            if word_set <= row1 or word_set <= row2 or word_set <= row3:
                words_in_rows.append(word)
        
        return words_in_rows