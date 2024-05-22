class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_str = ""
        length = len(s)

        for i, char in enumerate(s):
            # scenario 1
            left, right = i, i
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            
            sub_str_length = right - left - 1
            longest_str = longest_str if len(longest_str) >= sub_str_length else s[left+1:right]

            # scenario 2
            left, right = i, i+1
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            
            sub_str_length = right - left - 1
            longest_str = longest_str if len(longest_str) >= sub_str_length else s[left+1:right]
    
        return longest_str
