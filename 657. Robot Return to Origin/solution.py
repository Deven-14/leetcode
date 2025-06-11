class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for move in moves:
            match move:
                case 'R':
                    x += 1
                case 'L':
                    x -= 1
                case 'U':
                    y += 1
                case 'D':
                    y -= 1
        
        return x == 0 and y == 0


from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = Counter(moves)
        return directions['R'] == directions['L'] and directions['U'] == directions['D']
    

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')