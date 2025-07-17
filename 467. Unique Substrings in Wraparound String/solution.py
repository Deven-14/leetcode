from collections import defaultdict
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = defaultdict(int)
        dp[s[0]] = 1
        count = 1
        n = len(s)

        for i, j in zip(range(1, n), range(n-1)):
            count = count + 1 if (ord(s[i]) - ord(s[j])) % 26 == 1 else 1
            dp[s[i]] = max(dp[s[i]], count)
        
        return sum(dp.values())


from collections import defaultdict
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = defaultdict(int)
        dp[s[0]] = 1
        count = 1
        n = len(s)

        for i, j in zip(s[1:], s):
            count = count + 1 if (ord(i) - ord(j)) % 26 == 1 else 1
            dp[i] = max(dp[i], count)
        
        return sum(dp.values())