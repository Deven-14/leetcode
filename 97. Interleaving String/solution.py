from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
                
        @cache
        def helper(i, j, s):
            if i + j == l3:
                return s == s3
            
            if i < l1 and s1[i] == s3[i + j] and helper(i + 1, j, s + s1[i]):
                return True
            
            if j < l2 and s2[j] == s3[i + j] and helper(i, j + 1, s + s2[j]):
                return True

            return False
        
        return helper(0, 0, "")


# TODO: 1D DP and 2D DP solution