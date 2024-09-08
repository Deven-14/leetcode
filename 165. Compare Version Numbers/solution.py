from itertools import zip_longest
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = (int(num) for num in version1.split("."))
        version2_list = (int(num) for num in version2.split("."))
        
        for num1, num2 in zip_longest(version1_list, version2_list, fillvalue=0):
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        
        return 0
        

