from functools import cache
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        n = len(envelopes)
        
        @cache
        def helper(i, prev_envelope):
            if i == n:
                return 0
            
            max_env = 0 
            for j in range(i, n):
                envelope = envelopes[j]
                if envelope[0] > prev_envelope[0] and envelope[1] > prev_envelope[1]:
                    max_env = max(max_env, 1 + helper(j + 1, tuple(envelope)))
            
            return max_env

        max_env = 0
        for i in range(n):
            max_env = max(max_env, 1 + helper(i + 1, tuple(envelopes[i])))
        
        return max_env



# ! Time Limit Exceeded


from functools import cache
from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        n = len(envelopes)
        
        @cache
        def helper(prev_selected_idx):
            if prev_selected_idx == n:
                return 0
            
            max_env = 0 
            prev_envelope = envelopes[prev_selected_idx]
            for j in range(prev_selected_idx + 1, n):
                envelope = envelopes[j]
                if envelope[0] > prev_envelope[0] and envelope[1] > prev_envelope[1]:
                    max_env = max(max_env, 1 + helper(j))
            
            return max_env

        max_env = 0
        for i in range(n):
            max_env = max(max_env, 1 + helper(i))
        
        return max_env


# ! Time Limit Exceeded


from functools import cache
from bisect import bisect_right
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: x[1], reverse=True) # sort heights in decending order
        envelopes.sort(key=lambda x: x[0]) # sort widths in ascending order heights in desc
        n = len(envelopes)
        
        # after sorting, this problem is transforms to a longest increasing subsequence problem on their heights

        long_sub_seq = [envelopes[0][1]] # based on height
        for i in range(1, len(envelopes)):
            height = envelopes[i][1]

            if height > long_sub_seq[-1]:
                long_sub_seq.append(height)
            
            else:
                idx = bisect_left(long_sub_seq, height)
                long_sub_seq[idx] = height
            
        return len(long_sub_seq)


from functools import cache
from bisect import bisect_right
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1])) 
        # sort widths in ascending order, sort heights in decending order, combines into one
        # instead of 2 sorting (first on desc heights and second on asc widths)
        n = len(envelopes)
        
        # after sorting, this problem is transforms to a longest increasing subsequence problem on their heights

        long_sub_seq = [envelopes[0][1]] # based on height
        for i in range(1, len(envelopes)):
            height = envelopes[i][1]

            if height > long_sub_seq[-1]:
                long_sub_seq.append(height)
            
            else:
                idx = bisect_left(long_sub_seq, height)
                long_sub_seq[idx] = height
            
        return len(long_sub_seq)

        
# * this wasy of sorting makes the input [[5,4],[6,4],[6,7],[2,3]] to [[2,3],[5,4],[6,7],[6,5]]
# * now, heights [3,4,7,5] is a longest increasing subsequence
# * so the answer is 3, [3, 4, 7] or [3, 4, 5]
# * according to above LIS algo, we don't need to worry about 6 width getting in twice as it is sorting in descending
# * 6,7 will be added to the subsequence before 6,5 is considered, and 6,5 will be only replace 6,7 and won't increase the length of subsequence
# * so, the answer is 3
