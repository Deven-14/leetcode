class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [letter for letter in s.lower() if letter.isalnum()]
        n_2 = len(letters) // 2
        return letters[:n_2] == letters[:-n_2-1:-1]
