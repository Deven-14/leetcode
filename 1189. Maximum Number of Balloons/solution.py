from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        counts['l'] //= 2
        counts['o'] //= 2

        return min(counts['b'], counts['a'], counts['l'], counts['o'], counts['n'])