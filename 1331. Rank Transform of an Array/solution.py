class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = 1
        ranks = {}
        for ele in sorted(arr):
            if ele not in ranks:
                ranks[ele] = rank
                rank += 1
        
        return [ranks[ele] for ele in arr]


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = 1
        ranks = {}
        for ele in sorted(set(arr)):
            if ele not in ranks:
                ranks[ele] = rank
                rank += 1
        
        return [ranks[ele] for ele in arr]


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = { num: rank + 1 for rank, num in enumerate(sorted(set(arr))) }
        return [ranks[ele] for ele in arr]
        