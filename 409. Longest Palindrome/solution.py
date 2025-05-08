from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)

        is_odd_length_present = False
        longest_palindrome = 0
        for length in counts.values():
            if length % 2 == 0:
                longest_palindrome += length
            else:
                longest_palindrome += (length - 1)
                is_odd_length_present = True

        longest_palindrome += 1 if is_odd_length_present else 0
        return longest_palindrome