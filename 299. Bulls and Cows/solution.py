from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_secret = Counter(secret)
        count_guess = Counter(guess)

        common_count = (count_secret & count_guess).total()
        
        x = len([s for s, g in zip(secret, guess) if s == g])
        
        return f"{x}A{common_count-x}B"