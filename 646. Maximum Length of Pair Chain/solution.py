class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1], x[0]))

        count = 1
        prev_end = pairs[0][1]
        for start, end in pairs:
            if prev_end < start:
                count += 1
                prev_end = end
        
        return count


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        count = 1
        prev_end = pairs[0][1]
        for start, end in pairs:
            if prev_end < start:
                count += 1
                prev_end = end
        
        return count