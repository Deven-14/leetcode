class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        m = int(n * 0.05)
        return sum(arr[m:n-m]) / (n - (2 * m))