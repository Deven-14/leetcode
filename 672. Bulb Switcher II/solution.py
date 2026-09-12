class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0: return 1
        if n == 1: return 2
        if n == 2 and presses == 1: return 3
        if n == 2 or presses == 1: return 4
        if presses == 2: return 7
        if presses > 2: return 8


# https://leetcode.com/problems/bulb-switcher-ii/description/comments/1565085/
# https://leetcode.com/problems/bulb-switcher-ii/description/comments/2879347/
