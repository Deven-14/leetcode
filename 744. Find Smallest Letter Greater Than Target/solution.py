from bisect import bisect_right
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect_right(letters, target)
        if i == len(letters):
            return letters[0]
        
        return letters[i]