class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        idx = s.find('0')
        if idx == -1:
            return True
        return s.find('1', idx) == -1