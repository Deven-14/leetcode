class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""

        for letters in zip(*strs):
            if len(set(letters)) > 1:
                break
            lcp += letters[0]
        
        return lcp