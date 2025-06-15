class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        i, n = 1, len(s)

        while i < n:
            
            j = i - 1
            if s[i] == '0' and s[j] == '1':
                while i < n and j >= 0 and s[i] == '0' and s[j] == '1':
                    count += 1
                    i += 1
                    j -= 1
            
            elif s[i] == '1' and s[j] == '0':
                while i < n and j >= 0 and s[i] == '1' and s[j] == '0':
                    count += 1
                    i += 1
                    j -= 1
            
            else:
                i += 1
                    
        return count


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        curr_num_count = 1
        prev_num_count = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_num_count += 1
            else:
                count += min(curr_num_count, prev_num_count)
                prev_num_count = curr_num_count
                curr_num_count = 1
        
        return count + min(curr_num_count, prev_num_count)


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        curr_num = s[0]
        curr_num_count = 1
        prev_num_count = 0

        for i in range(1, len(s)):
            if s[i] == curr_num:
                curr_num_count += 1
            else:
                count += min(curr_num_count, prev_num_count)
                prev_num_count = curr_num_count
                curr_num = s[i]
                curr_num_count = 1
        
        return count + min(curr_num_count, prev_num_count)