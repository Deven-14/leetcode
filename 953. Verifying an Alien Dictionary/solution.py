import string
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        trans = str.maketrans(order, string.ascii_lowercase)
        trans_words = [word.translate(trans) for word in words]

        return trans_words == sorted(trans_words)


import string
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        trans = str.maketrans(order, string.ascii_lowercase)
        trans_words = [word.translate(trans) for word in words]

        return all(trans_words[i-1] <= trans_words[i] for i in range(1, len(words)))


