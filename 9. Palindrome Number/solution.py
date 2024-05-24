class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        mid = len(x_str)//2
        if len(x_str) % 2 != 0:
            return x_str[:mid] == x_str[:mid:-1]
        else:
            return x_str[:mid] == x_str[:mid-1:-1]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num, rev = x, 0
        while num != 0:
            rev = rev*10 + num%10
            num //= 10

        return x == rev