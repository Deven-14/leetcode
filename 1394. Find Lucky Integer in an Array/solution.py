from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        for ele, count in counts.most_common():
            if ele == count:
                return ele
        return -1