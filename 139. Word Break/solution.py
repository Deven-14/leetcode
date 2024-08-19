class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def helper(s):
            if len(s) == 0:
                return True
            
            for word in wordDict:
                if s.startswith(word) and helper(s[len(word):]):
                    return True
            
            return False
        
        return helper(s)


# ! timeout on the above solution


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def helper(s):
            if len(s) == 0:
                return True
            
            for word in wordDict:
                if s.startswith(word) and helper(s[len(word):]):
                    return True
            
            return False
        
        return helper(s)

# * THE SOLUTION WAS CACHING