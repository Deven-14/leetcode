from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d_banned = 0
        r_banned = 0
        queue = deque(senate)
        r_count = senate.count('R')
        d_count = senate.count('D')

        while queue and r_banned < r_count and d_banned < d_count:
            senator = queue.popleft()
            if senator == "D":
                if d_banned > 0:
                    d_banned -= 1
                    continue
                r_banned += 1
            else:
                if r_banned > 0:
                    r_banned -= 1
                    continue
                d_banned += 1
            queue.append(senator)

        if r_banned == r_count:
            return "Dire"

        return "Radiant"



from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d_banned = 0
        r_banned = 0
        queue = deque(senate)
        r_count = senate.count('R')
        d_count = senate.count('D')

        while queue and r_banned < r_count and d_banned < d_count:
            senator = queue.popleft()
            if senator == "D":
                if d_banned > 0:
                    d_banned -= 1
                    d_count -= 1
                    continue
                r_banned += 1
            else:
                if r_banned > 0:
                    r_banned -= 1
                    r_count -= 1
                    continue
                d_banned += 1
            queue.append(senator)

        if r_banned == r_count:
            return "Dire"

        return "Radiant"



from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d_banned = 0
        r_banned = 0
        queue = deque(senate)
        r_count = senate.count('R')
        d_count = senate.count('D')

        while queue and r_count > 0 and d_count > 0:
            senator = queue.popleft()
            if senator == "D":
                if d_banned > 0:
                    d_banned -= 1
                    d_count -= 1
                    continue
                r_banned += 1
            else:
                if r_banned > 0:
                    r_banned -= 1
                    r_count -= 1
                    continue
                d_banned += 1
            queue.append(senator)

        if d_count > 0:
            return "Dire"

        return "Radiant"



from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d_banned = 0
        r_banned = 0
        queue = deque(senate)
        r_count = senate.count('R')
        d_count = senate.count('D')

        while r_count > 0 and d_count > 0:
            senator = queue.popleft()
            if senator == "D":
                if d_banned > 0:
                    d_banned -= 1
                    d_count -= 1
                    continue
                r_banned += 1
            else:
                if r_banned > 0:
                    r_banned -= 1
                    r_count -= 1
                    continue
                d_banned += 1
            queue.append(senator)

        if d_count > 0:
            return "Dire"

        return "Radiant"