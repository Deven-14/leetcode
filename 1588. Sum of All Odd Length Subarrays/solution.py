class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_arr = list(accumulate(arr, initial=0))
        n = len(arr)
        total_sum = 0

        for l in range(1, n + 1, 2):
            for i in range(n - l + 1):
                total_sum += prefix_arr[i + l] - prefix_arr[i]
        
        return total_sum
        