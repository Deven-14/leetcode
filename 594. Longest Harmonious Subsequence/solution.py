from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_sub_seq = 0
        for num, count in counts.items():
            if num-1 in counts:
                max_sub_seq = max(max_sub_seq, count + counts[num-1])
            if num+1 in counts:
                max_sub_seq = max(max_sub_seq, count + counts[num+1])
        
        return max_sub_seq


from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_sub_seq = 0
        for num, count in counts.items():
            if num+1 in counts:
                max_sub_seq = max(max_sub_seq, count + counts[num+1])
        
        return max_sub_seq