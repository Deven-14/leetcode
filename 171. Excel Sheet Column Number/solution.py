class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber = 0
        m = 1
        for i in range(len(columnTitle)-1, -1, -1):
            columnNumber += (ord(columnTitle[i]) - 64) * m
            m *= 26
        
        return columnNumber