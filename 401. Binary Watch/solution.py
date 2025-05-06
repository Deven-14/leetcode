class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        leds = [1, 2, 4, 8, 16, 32, 1, 2, 4, 8]
        combinations = []

        def backtrack(i, j, total_hours, total_mins):
            if total_hours > 11 or total_mins > 59:
                return

            if i == turnedOn:
                combinations.append(f"{total_hours}:{str(total_mins).zfill(2)}")
                return
            
            if j > 9:
                return
            
            if j > 5:
                backtrack(i+1, j+1, total_hours + leds[j], total_mins)
                backtrack(i, j+1, total_hours, total_mins)
            else:
                backtrack(i+1, j+1, total_hours, total_mins + leds[j])
                backtrack(i, j+1, total_hours, total_mins)

        backtrack(0, 0, 0, 0)
        return combinations
            

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        leds = [1, 2, 4, 8, 16, 32, 1, 2, 4, 8]
        combinations = []

        def backtrack(i, j, total_hours, total_mins):
            if total_hours > 11 or total_mins > 59:
                return

            if i == turnedOn:
                combinations.append(f"{total_hours}:{total_mins:02d}")
                return
            
            if j > 9:
                return
            
            if j > 5:
                backtrack(i+1, j+1, total_hours + leds[j], total_mins)
                backtrack(i, j+1, total_hours, total_mins)
            else:
                backtrack(i+1, j+1, total_hours, total_mins + leds[j])
                backtrack(i, j+1, total_hours, total_mins)

        backtrack(0, 0, 0, 0)
        return combinations
            

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        leds = [1, 2, 4, 8, 16, 32, 1, 2, 4, 8]
        combinations = []

        def backtrack(i, j, total_hours, total_mins):
            if total_hours > 11 or total_mins > 59:
                return

            if i == turnedOn:
                combinations.append(f"{total_hours}:{total_mins:02d}")
                return
            
            if j > 9 or i > turnedOn:
                return
            
            if j > 5:
                backtrack(i+1, j+1, total_hours + leds[j], total_mins)
                backtrack(i, j+1, total_hours, total_mins)
            else:
                backtrack(i+1, j+1, total_hours, total_mins + leds[j])
                backtrack(i, j+1, total_hours, total_mins)

        backtrack(0, 0, 0, 0)
        return combinations
            
            