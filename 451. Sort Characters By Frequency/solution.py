from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        new_s = []
        for char, count in counts.most_common():
            new_s.append(char * count)
        
        return "".join(new_s)

# same solution with dict:
# use dict to count and then sort the dict.items()
# and then do the same for loop as above