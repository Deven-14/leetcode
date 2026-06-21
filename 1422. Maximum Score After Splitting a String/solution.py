class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        left, right = 0, ones
        score = float('-inf')

        for digit in s[:-1]:
            if digit == '0':
                left += 1
            else:
                right -= 1
            score = max(score, left + right)
        
        return score