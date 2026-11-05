class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        set_s = set(s)

        not_nice_set = set()
        for char in s:
            if char.lower() not in set_s or char.upper() not in set_s:
                not_nice_set.add(char.lower())
                not_nice_set.add(char.upper())
        
        if not not_nice_set:
            return s
        
        count = 0
        max_len_substr = ""
        substr = []
        for char in s:
            if char in not_nice_set:
                sub_substr = self.longestNiceSubstring("".join(substr))
                if len(sub_substr) > len(max_len_substr):
                    max_len_substr = sub_substr
                substr = []
            else:
                substr.append(char)
        
        if substr:
            sub_substr = self.longestNiceSubstring("".join(substr))
            if len(sub_substr) > len(max_len_substr):
                max_len_substr = sub_substr
    
        return max_len_substr



class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s: return ""

        set_s = set(s)
        for i, char in enumerate(s):
            if char.swapcase() not in set_s:
                sub1 = self.longestNiceSubstring(s[:i])
                sub2 = self.longestNiceSubstring(s[i+1:])
                return max(sub1, sub2, key=len)
        
        return s

