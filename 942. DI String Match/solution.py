class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start, end = 0, len(s)
        perm = []
        for char in s:
            if char == "I":
                perm.append(start)
                start += 1
            else:
                perm.append(end)
                end -= 1
        
        if s[-1] == "I":
            perm.append(start)
            start += 1
        else:
            perm.append(end)
            end -= 1
        
        return perm