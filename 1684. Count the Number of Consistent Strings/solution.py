class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(1 for word in words if set(word) <= allowed)


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)

        def isWordAllowed(word):
            for char in word:
                if char not in allowed:
                    return False
            return True
        
        return sum(isWordAllowed(word) for word in words)


