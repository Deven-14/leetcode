class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexi_order = []

        def dfs(num_str):

            for i in range(10):
                t_str = num_str + str(i)
                num = int(t_str)
                if num > n:
                    break
                
                lexi_order.append(num)
                dfs(t_str)
        
        for i in range(1, 10):
            if i > n:
                break
            lexi_order.append(i)
            dfs(str(i))
        
        return lexi_order


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexi_order = []
        num = 1

        for _ in range(n):
            lexi_order.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num >= n:
                    num //= 10
                num += 1
        
        return lexi_order
    

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexi_order = []
        num = 1

        for _ in range(n):
            lexi_order.append(num)
            if (t := num * 10) <= n:
                num = t
            else:
                while num % 10 == 9 or num >= n:
                    num //= 10
                num += 1
        
        return lexi_order