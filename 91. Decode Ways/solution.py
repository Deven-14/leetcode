class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0":
            return 0

        s2 = [int(s[0])]
        for i in range(1, n):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    s2[-1] = None
                    s2.append(None)
                else:
                    return 0
            else:
                s2.append(int(s[i]))
        
        last = n-1
        counts = [1] * (n+1)
        def dfs(i = 0): # memoization
            if i >= last:
                return 1
            
            count = dfs(i+1)
            
            if s2[i+1] != None and (s2[i] == 1 or (s2[i] == 2 and s2[i+1] <= 6)):
                count += counts[i+2]

            counts[i] = count
            return count
        
        return dfs()


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0":
            return 0

        s2 = [int(s[0])]
        for i in range(1, n):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    s2[-1] = None
                    s2.append(None)
                else:
                    return 0
            else:
                s2.append(int(s[i]))
        
        counts = [1] * (n+1)
        for i in range(n-2, -1, -1):
            count = counts[i+1]
            
            if s2[i+1] != None and (s2[i] == 1 or (s2[i] == 2 and s2[i+1] <= 6)):
                count += counts[i+2]

            counts[i] = count
        
        return counts[0]


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0":
            return 0
        
        dp = [0] * (n+1)
        dp[-1] = 1 # extra node
        dp[-2] = 1 # last node
        for i in range(n-2, -1, -1):
            dp[i] = dp[i+1]
            
            if s[i+1] != "0" and (s[i] == "1" or (s[i] == "2" and s[i+1] <= "6")):
                dp[i] += dp[i+2]
        
        return dp[0]

