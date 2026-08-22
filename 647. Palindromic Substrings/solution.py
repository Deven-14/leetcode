class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = n

        for i in range(n):
            dp[i][i] = True
        
        for j in range(1, n):
            for i in range(n-j):
                col = i + j
                if (dp[i][col-1] == dp[i+1][col]) and s[i:col] == s[i+1:col+1][::-1]:
                    dp[i][col] = True
                    count += 1
        
        return count

# * only beats 5% of solutions


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = n

        # single char
        for i in range(n):
            dp[i][i] = True
        
        # 2 chars
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1
        
        # 3 to n chars
        for j in range(2, n):
            for i in range(n-j):
                col = i + j
                if (s[i] == s[col]) and dp[i+1][col-1]:
                    dp[i][col] = True
                    count += 1
        
        return count

# * beats 30% of cases

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = n

        # single char
        for i in range(n):
            dp[i][i] = True
        
        # 2 chars
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1
        
        # length [3, n] chars => in index => [2, n)
        for l in range(2, n):
            for i in range(n-l):
                j = i + l # col / last index of the string
                if (s[i] == s[j]) and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1
        
        return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        def count_sub_palindromes(l, r):
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            return count
        
        count = 0
        for i in range(n):
            count += count_sub_palindromes(i, i)
            count += count_sub_palindromes(i, i+1)
        
        return count

# * beats 90%


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        if len(set(s)) == 1:
            return (n * (n+1)) // 2
        
        def count_sub_palindromes(l, r):
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            return count
        
        count = 0
        for i in range(n):
            count += count_sub_palindromes(i, i)
            count += count_sub_palindromes(i, i+1)
        
        return count


# * beats 98%









# Tried the question again

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = n

        # length 1
        for i in range(n):
            dp[i][i] = True
        
        # length 2
        for i in range(1, n):
            if s[i] == s[i-1]:
                dp[i-1][i] = True
                count += 1
        
        # length 3 to n => idx [2, n)
        for l in range(2, n):
            for i in range(n - l): # row
                j = i + l # col
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
        
        return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = n

        def count_palindromes(i, j):
            c = 0
            while i >= 0 and j < n and s[i] == s[j]:
                c += 1
                i -= 1
                j += 1
            return c

    
        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += count_palindromes(i - 2, i + 1) + 1
            count += count_palindromes(i - 1, i + 1)

        return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def count_palindromes(i, j):
            c = 0
            while i >= 0 and j < n and s[i] == s[j]:
                c += 1
                i -= 1
                j += 1
            return c

    
        for i in range(n):
            count += count_palindromes(i, i)
            count += count_palindromes(i - 1, i)

        return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n <= 1: return n
        if len(set(s)) == 1: return n * (n + 1) // 2

        def count_palindromes(i, j):
            c = 0
            while i >= 0 and j < n and s[i] == s[j]:
                c += 1
                i -= 1
                j += 1
            return c

        count = 0
        for i in range(n):
            count += count_palindromes(i, i)
            count += count_palindromes(i - 1, i)

        return count



