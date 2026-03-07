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
            

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        n = len(t)
        tcount = Counter(t)
        wcount = Counter(s[:n])
        req_match_count = len(tcount)
        curr_match_count = sum(tcount[char] <= wcount[char] for char in tcount)
        if curr_match_count == req_match_count:
            return s[:n]
        
        total = s + t
        min_window = total

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
            
            if curr_match_count < req_match_count:
                break

            if (i - j) < len(min_window):
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
            
        return "" if min_window == total else min_window
            


from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        n = len(t)
        tcount = Counter(t)
        wcount = Counter(s[:n])
        req_match_count = len(tcount)
        curr_match_count = sum(tcount[char] <= wcount[char] for char in tcount)
        if curr_match_count == req_match_count:
            return s[:n]
        
        min_window = s
        found = False

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
            
            if curr_match_count < req_match_count:
                break

            found = True
            if (i - j) < len(min_window):
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
            
        return min_window if found else ""
            


from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        n = len(t)
        tcount = Counter(t)
        wcount = Counter(s[:n])
        req_match_count = len(tcount)
        curr_match_count = sum(tcount[char] <= wcount[char] for char in tcount)
        if curr_match_count == req_match_count:
            return s[:n]
        
        min_window = s
        found = False

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
            
            if curr_match_count < req_match_count:
                break

            found = True
            if (i - j) < len(min_window):
                min_window = s[j:i]

            while j < i and curr_match_count == req_match_count:
                removed_char = s[j]
                if removed_char in tcount:
                    if wcount[removed_char] == tcount[removed_char]:
                        curr_match_count -= 1
                    wcount[removed_char] -= 1
                j += 1
            
            if (i - j + 1) < len(min_window):
                min_window = s[j-1:i]
            
        return min_window if found else ""
            

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(t), len(s)
        if m < n:
            return ""
        
        tcount = Counter(t)
        match_counter = n
        start = 0
        min_length = float('inf')

        l, r = 0, 0
        while r < m:
            new_char = s[r]

            if tcount[new_char] > 0:
                match_counter -= 1

            tcount[new_char] -= 1
            r += 1

            while match_counter == 0:
                if (length := r - l) < min_length:
                    start = l
                    min_length = length
                
                removed_char = s[l]
                tcount[removed_char] += 1
                if tcount[removed_char] > 0:
                    match_counter += 1
                l += 1
            
        return "" if min_length == float('inf') else s[start:start+min_length]
            


from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(t), len(s)
        if m < n:
            return ""
        
        tcount = Counter(t)
        match_counter = n
        start = 0
        min_length = float('inf')

        l, r = 0, 0
        while r < m:
            if tcount[s[r]] > 0:
                match_counter -= 1

            tcount[s[r]] -= 1
            r += 1

            while match_counter == 0:
                if (length := r - l) < min_length:
                    start = l
                    min_length = length
                
                tcount[s[l]] += 1
                if tcount[s[l]] > 0:
                    match_counter += 1
                l += 1
            
        return "" if min_length == float('inf') else s[start:start + min_length]
            


from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(t), len(s)
        if m < n:
            return ""
        
        tcount = Counter(t)
        match_counter = n
        start = 0
        min_length = float('inf')

        l, r = 0, 0
        while r < m:

            while r < m and match_counter != 0:
                if tcount[s[r]] > 0:
                    match_counter -= 1

                tcount[s[r]] -= 1
                r += 1
            
            if match_counter != 0:
                break

            while match_counter == 0:
                tcount[s[l]] += 1
                if tcount[s[l]] > 0:
                    match_counter += 1
                l += 1
            
            if (length := r - l + 1) < min_length:
                start = l-1
                min_length = length
            
            
        return "" if min_length == float('inf') else s[start:start + min_length]
            


from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(t), len(s)
        if m < n:
            return ""
        
        tcount = [0] * 128
        for char in t.encode():
            tcount[char] += 1
        sbytes = s.encode()
        match_counter = n
        start = 0
        min_length = float('inf')

        l, r = 0, 0
        while r < m:

            while r < m and match_counter != 0:
                if tcount[sbytes[r]] > 0:
                    match_counter -= 1

                tcount[sbytes[r]] -= 1
                r += 1
            
            if match_counter != 0:
                break

            while match_counter == 0:
                tcount[sbytes[l]] += 1
                if tcount[sbytes[l]] > 0:
                    match_counter += 1
                l += 1
            
            if (length := r - l + 1) < min_length:
                start = l-1
                min_length = length
            
            
        return "" if min_length == float('inf') else s[start:start + min_length]
            

# https://leetcode.com/problems/minimum-window-substring/solutions/26808/here-is-a-10-line-template-that-can-solv-lct0

# For most substring problem, we are given a string and need to find a substring of it which satisfy some restrictions. A general way is to use a hashmap assisted with two pointers. The template is given below.