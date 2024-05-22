class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        longest_length = 0
        start, end = 0, 0 # sliding window

        for char in s:
            if char not in unique_chars:
                unique_chars.add(char)
            else:
                longest_length = max(longest_length, end - start)

                while s[start] != char:
                    unique_chars.remove(s[start])
                    start += 1
                
                start += 1
            
            end += 1  

        longest_length = max(longest_length, end - start)
        return longest_length            