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


# First, I count the number of 1 or 0 grouped consecutively.
# For example "0110001111" will be [1, 2, 3, 4].

# Second, for any possible substrings with 1 and 0 grouped consecutively, the number of valid substring will be the minimum number of 0 and 1.
# For example "0001111", will be min(3, 4) = 3, ("01", "0011", "000111")