class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        def diff(start):
            count = 0
            expected_char = start
            for char in s:
                if char != expected_char:
                    count += 1
                expected_char = '1' if expected_char == '0' else '0'
            return count
        
        return min(diff('0'), diff('1'))


class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        is_odd = n % 2
        mid = n // 2
        alt_s1 = '01' * mid + ('0' if is_odd else '')
        alt_s2 = '10' * mid + ('1' if is_odd else '')

        def diff(expected_s):
            return sum(
                char != expected_char
                for char, expected_char in zip(s, expected_s)
            )
            
        return min(diff(alt_s1), diff(alt_s2))


