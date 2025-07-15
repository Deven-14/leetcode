from collections import Counter
import operator
from functools import reduce
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars_count = reduce(operator.__and__, (Counter(word) for word in words))
        common_chars = []
        for char, count in common_chars_count.items():
            common_chars.extend(char * count)
        return common_chars