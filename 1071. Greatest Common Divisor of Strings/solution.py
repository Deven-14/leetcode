class Solution:

    def gcd(m, n):
        if m < n:
            m, n = n, m
        
        while n:
            m, n = n, m % n
        
        return m


    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        n = gcd(len(str1), len(str2))

        return str1[:n]
