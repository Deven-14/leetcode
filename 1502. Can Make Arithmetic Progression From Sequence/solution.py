class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
            
        return True


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        a = min(arr)
        an = max(arr)
        sn = n * (a + an) / 2
        if sn % 1 != 0: # if not int
            return False
        
        diff = (an - a) / (n - 1)
        if diff % 1 != 0:
            return False
        
        arr_set = set(arr)
        for i in range(1, n):
            if (a + i * diff) not in arr_set:
                return False
        
        return True

# a_n = a + (n - 1)d
# 𝑆𝑛=𝑛/2[2𝑎+(𝑛−1)𝑑]
# S_n = n/2(a + a_n)
        
