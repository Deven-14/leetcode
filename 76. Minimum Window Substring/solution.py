from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        n = len(t)
        tcount = Counter(t)
        if tcount != (Counter(s) & tcount):
            return ""

        wcount = Counter(s[:n])
        req_match_count = len(tcount)
        curr_match_count = sum(tcount[char] <= wcount[char] for char in tcount)
        if curr_match_count == req_match_count:
            return s[:n]
        
        min_window = s

        m = len(s)
        i, j = n, 0
        while i < m:

            while i < m and curr_match_count < req_match_count:
                new_char = s[i]
                if new_char in tcount:
                    wcount[new_char] += 1
                    if wcount[new_char] == tcount[new_char]:
                        curr_match_count += 1
                i += 1
            
            if curr_match_count == req_match_count and (i - j) < len(min_window):
                min_window = s[j:i]

            while j < i and curr_match_count == req_match_count:
                removed_char = s[j]
                if removed_char in tcount:
                    wcount[removed_char] -= 1
                    if wcount[removed_char] < tcount[removed_char] and wcount[removed_char]+1 == tcount[removed_char]:
                        curr_match_count -= 1
                j += 1
            
            if (i - j + 1) < len(min_window):
                min_window = s[j-1:i]
            
        return min_window
            
