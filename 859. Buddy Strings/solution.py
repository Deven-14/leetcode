from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal and any(count > 1 for count in Counter(s).values()):
            return True
        
        c = 0
        idx = []
        for i, (char1, char2) in enumerate(zip(s, goal)):
            if char1 != char2:
                c += 1
                idx.append(i)
                if c > 2:
                    return False
        
        return c == 2 and s[idx[0]] == goal[idx[1]] and s[idx[1]] == goal[idx[0]]


from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal and any(count > 1 for count in Counter(s).values()):
            return True
        
        mismatch = [(char1, char2) for char1, char2 in zip(s, goal) if char1 != char2]
        
        return len(mismatch) == 2 and mismatch[0][0] == mismatch[1][1] and mismatch[0][1] == mismatch[1][0]