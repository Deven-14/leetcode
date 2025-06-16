from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counts = Counter(s)
        
        for char, count in counts.items():
            if count < k:
                idx = s.find(char)
                left_max = self.longestSubstring(s[:idx], k)
                right_max = self.longestSubstring(s[idx+1:], k)
                return max(left_max, right_max)
        
        return len(s)
        

from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def helper(substr):
            if len(substr) < k:
                return 0
            
            counts = Counter(substr)
            indices = [i for i, char in enumerate(substr) if counts[char] < k]

            if not indices:
                return len(substr)
            
            max_len = helper(substr[:indices[0]])
            for i in range(1, len(indices)):
                max_len = max(max_len, helper(substr[indices[i-1] + 1:indices[i]]))
            
            max_len = max(max_len, helper(substr[indices[-1] + 1:]))
        
            return max_len
        
        return helper(s)
        
# Why sliding window works for this qustion and how it works? Simple analysis.
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solutions/2821874/why-sliding-window-works-for-this-qustion-and-how-it-works-simple-analysis