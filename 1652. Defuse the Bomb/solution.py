class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        if k == 0: return [0] * len(code)

        ans = []
        n = len(code)
        if k > 0:
            window = sum(code[1:k + 1])
            ans.append(window)
            for i in range(1, n):
                window -= code[i]
                window += code[(i + k) % n]
                ans.append(window)
            return ans
        
        window = sum(code[k:])
        ans.append(window)
        for i in range(n-1):
            window -= code[(n + k + i) % n]
            window += code[i]
            ans.append(window)
        return ans