class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                if abs(arr[i] - arr[j]) > a:
                    continue
                
                for k in range(j+1, n):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    
                    if abs(arr[i] - arr[k]) <= c:
                        count += 1
        
        return count


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        prefix_sum_freq = [0] * 1001

        for j in range(n):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) > b:
                    continue
                
                lj, rj = arr[j] - a, arr[j] + a
                lk, rk = arr[k] - c, arr[k] + c
                l = max(0, lj, lk)
                r = min(1000, rj, rk)

                if l <= r:
                    count += prefix_sum_freq[r] if l == 0 else prefix_sum_freq[r] - prefix_sum_freq[l - 1]
            
            for k in range(arr[j], 1001):
                prefix_sum_freq[k] += 1
            
        return count

