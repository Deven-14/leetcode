class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k == 1:
            return list(range(1, n + 1))
        
        arr = list(range(1, n - k))
        arr2 = list(range(1, k + 2)) # k + 2 = (k + 1) + 1, + 1 outside as we are starting from 1
        mid = math.ceil((k + 1) / 2)
        arr3 = [0] * (k + 1)
        arr3[::2] = arr2[:mid]
        arr3[1::2] = arr2[mid:][::-1]
        m = len(arr)
        return arr + [ele + m for ele in arr3]

# https://leetcode.com/problems/beautiful-arrangement-ii/solutions/127567/beautiful-arrangement-ii-by-leetcode-akkq