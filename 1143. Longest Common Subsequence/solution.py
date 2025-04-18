class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1) + 1, len(text2) + 1
        dp = [[0] * l2 for _ in range(l1)]

        for i in range(1, l1):
            for j in range(1, l2):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[l1-1][l2-1]


class Solution:

    def remove_uncommon_chars(self, text1, text2):
        s1, s2 = set(text1), set(text2)
        new_text1 = [char for char in text1 if char in s2]
        new_text2 = [char for char in text2 if char in s1]
        return "".join(new_text1), "".join(new_text2)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1, text2 = self.remove_uncommon_chars(text1, text2)
        l1, l2 = len(text1) + 1, len(text2) + 1
        dp = [[0] * l2 for _ in range(l1)]

        for i in range(1, l1):
            for j in range(1, l2):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[l1-1][l2-1]
