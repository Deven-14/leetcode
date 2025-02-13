class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_set = [set(word) for word in words]
        n = len(words_set)

        max_word_len = 0
        for i in range(n):
            len_word = len(words[i])
            word_set = words_set[i]
            for j in range(i+1, n):
                if word_set.isdisjoint(words_set[j]):
                    max_word_len = max(max_word_len, len_word * len(words[j]))
        
        return max_word_len
