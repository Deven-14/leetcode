import string
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        trans = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        s = paragraph.translate(trans)
        counts = Counter(s.lower().split())
        banned = set(banned)
        for key, value in counts.most_common():
            if key not in banned:
                return key
        
