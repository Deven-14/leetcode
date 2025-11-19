from collections import Counter
class DetectSquares:

    def __init__(self):
        self.xaxis = defaultdict(Counter)
        self.yaxis = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xaxis[x][y] += 1
        self.yaxis[y][x] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        
        count = 0
        for y2 in self.xaxis[x1]:
            diff = abs(y2 - y1)
            if diff == 0:
                continue

            x2 = x1 + diff
            count += self.yaxis[y2][x2] * self.yaxis[y2][x1] * self.xaxis[x2][y1]
            
            x2 = x1 - diff
            count += self.yaxis[y2][x2] * self.yaxis[y2][x1] * self.xaxis[x2][y1]
        
        return count
            

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


from collections import Counter
class DetectSquares:

    def __init__(self):
        self.xaxis = defaultdict(Counter)
        self.yaxis = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xaxis[x][y] += 1
        self.yaxis[y][x] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        
        count = 0
        for y2 in self.xaxis[x1]:
            if y1 == y2:
                continue

            diff = abs(y2 - y1)
            
            x2 = x1 + diff
            count += self.yaxis[y2][x2] * self.yaxis[y2][x1] * self.xaxis[x2][y1]
            
            x2 = x1 - diff
            count += self.yaxis[y2][x2] * self.yaxis[y2][x1] * self.xaxis[x2][y1]
        
        return count
            

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


from collections import Counter
class DetectSquares:

    def __init__(self):
        self.xaxis = defaultdict(Counter)
        self.yaxis = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xaxis[x][y] += 1
        self.yaxis[y][x] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        
        count = 0
        for y2, pt_count in self.xaxis[x1].items():
            if y1 == y2:
                continue

            diff = abs(y2 - y1)

            x2 = x1 + diff
            count += self.yaxis[y2][x2]* self.xaxis[x2][y1] * pt_count
            
            x2 = x1 - diff
            count += self.yaxis[y2][x2] * self.xaxis[x2][y1] * pt_count
        
        return count
            

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


from collections import Counter
class DetectSquares:

    def __init__(self):
        self.xaxis = defaultdict(Counter)
        self.yaxis = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xaxis[x][y] += 1
        self.yaxis[y][x] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        
        count = 0
        for y2, pt_count in self.xaxis[x1].items():
            if y1 == y2:
                continue

            diff = abs(y2 - y1)

            x2 = x1 + diff
            if self.yaxis[y2][x2] and self.xaxis[x2][y1]:
                count += self.yaxis[y2][x2] * self.xaxis[x2][y1] * pt_count
            
            x2 = x1 - diff
            if self.yaxis[y2][x2] and self.xaxis[x2][y1]:
                count += self.yaxis[y2][x2] * self.xaxis[x2][y1] * pt_count
        
        return count
            

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)