class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        max_idx = 0
        for i in range(n):
            if arrays[i][-1] > arrays[max_idx][-1]:
                max_idx = i
        
        min_idx = 0 if max_idx != 0 else 1
        for i in range(n):
            if arrays[i][0] < arrays[min_idx][0] and i != max_idx:
                min_idx = i
        
        res1 = abs(arrays[max_idx][-1] - arrays[min_idx][0])

        min_idx = 0
        for i in range(n):
            if arrays[i][0] < arrays[min_idx][0]:
                min_idx = i

        max_idx = 0 if min_idx != 0 else 1
        for i in range(n):
            if arrays[i][-1] > arrays[max_idx][-1] and i != min_idx:
                max_idx = i
        
        res2 = abs(arrays[max_idx][-1] - arrays[min_idx][0])
        return max(res1, res2)
        
        

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        max_idx1, min_idx1 = 0, 0
        for i in range(n):
            if arrays[i][-1] > arrays[max_idx1][-1]:
                max_idx1 = i
            if arrays[i][0] < arrays[min_idx1][0]:
                min_idx1 = i
        
        if max_idx1 != min_idx1:
            return abs(arrays[max_idx1][-1] - arrays[min_idx1][0])

        max_idx2, min_idx2 = 0 if max_idx1 != 0 else 1, 0 if min_idx1 != 0 else 1
        for i in range(n):
            if arrays[i][0] < arrays[min_idx2][0] and i != min_idx1:
                min_idx2 = i
            if arrays[i][-1] > arrays[max_idx2][-1] and i != max_idx1:
                max_idx2 = i
        
        return max(
            abs(arrays[max_idx1][-1] - arrays[min_idx2][0]),
            abs(arrays[max_idx2][-1] - arrays[min_idx1][0]),
        )


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_ele, min_ele = arrays[0][-1], arrays[0][0]
        res = 0

        for arr in arrays[1:]:
            res = max(
                res,
                max_ele - arr[0],
                arr[-1] - min_ele
            )
            max_ele = max(max_ele, arr[-1])
            min_ele = min(min_ele, arr[0])
        
        return res