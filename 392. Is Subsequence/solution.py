class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_t = len(t)
        len_s = len(s)

        if len_t == 0 and len_s == 0:
            return True
        elif len_t == 0:
            return False
        elif len_s == 0:
            return True

        dp = [[False] * len_t for _ in range(len_s)]

        char = s[0]
        prev_char_found_idx = 0
        for i in range(len_t):
            if t[i] == char:
                prev_char_found_idx = i
                dp[0][i:] = [True] * (len_t - i)
                break

        for i in range(1, len_s):
            char = s[i]
            for j in range(prev_char_found_idx + 1, len_t):
                if t[j] == char and dp[i-1][j-1] is True:
                    prev_char_found_idx = j
                    dp[i][j:] = [True] * (len_t - j)
                    break
        
        return dp[len_s-1][len_t-1]


# dp solution above

# could be done simpler by recusion 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        
        def helper(s_char_idx, t_char_idx):
            if s_char_idx == len_s:
                return True
            
            char = s[s_char_idx]
            for i in range(t_char_idx, len_t):
                if t[i] == char:
                    return helper(s_char_idx + 1, i + 1)
            
            return False
        
        return helper(0, 0)


# could be done easier with two pointers

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        len_s, len_t = len(s), len(t)

        while i < len_s and j < len_t:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len_s