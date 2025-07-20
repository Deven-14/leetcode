class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        
        partition = total // 3
        i, n = 0, len(arr)
        count = 0

        while i < n and count < 3:

            total = arr[i]
            i += 1
            while i < n and total != partition:
                total += arr[i]
                i += 1
            
            if total == partition:
                count += 1
        
        return count == 3 and (i == n or sum(arr[i:]) == 0)


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        
        partition = total // 3
        left_sum, right_sum = arr[0], arr[-1]
        n = len(arr)
        l, r = 1, n-2

        while l < r and left_sum != partition:
            left_sum += arr[l]
            l += 1
        
        while l < r and right_sum != partition:
            right_sum += arr[r]
            r -= 1
        
        return left_sum == partition == right_sum