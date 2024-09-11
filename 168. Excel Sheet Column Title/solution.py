class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columns = ["-", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        column = ""
        while columnNumber > 0:
            n, columnNumber = divmod(columnNumber, 26)
            if columnNumber != 0:
                column += columns[columnNumber]
            else:
                n -= 1
                column += columns[26]
            columnNumber = n
        
        return column[::-1]


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columns = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        columnTitle = ""
        while columnNumber > 0:
            n, columnNumber = divmod(columnNumber, 26)
            if columnNumber != 0:
                columnTitle += columns[columnNumber]
            else:
                n -= 1
                columnTitle += columns[26]
            columnNumber = n
        
        return columnTitle[::-1]

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columns = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        columnTitle = ""
        while columnNumber > 0:
            n, columnNumber = divmod(columnNumber-1, 26)
            columnTitle += columns[1+columnNumber]
            columnNumber = n
        
        return columnTitle[::-1]
    
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columns = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        columnTitle = ""
        while columnNumber > 0:
            n, columnNumber = divmod(columnNumber-1, 26)
            columnTitle = columns[1+columnNumber] + columnTitle
            columnNumber = n
        
        return columnTitle