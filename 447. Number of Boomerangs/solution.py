from collections import Counter
from math import sqrt, perm
class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0

        def distance(p1, p2):
            (x1, y1) = p1
            (x2, y2) = p2
            return sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
        n = len(points)
        boomerangs = 0

        for p1 in points:
            distances = Counter()
            for p2 in points:
                distances[distance(p1, p2)] += 1
            
            for d, count in distances.items():
                if count == 2:
                    boomerangs += 2
                elif count > 2:
                    boomerangs += perm(count, 2)
            
        return boomerangs

from collections import Counter
from math import sqrt, perm
class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0

        n = len(points)
        boomerangs = 0

        for (x1, y1) in points:
            distances = Counter()
            for (x2, y2) in points:
                d1 = (x2 - x1)
                d2 = (y2 - y1)
                d = sqrt(d1*d1 + d2* d2)
                distances[d] += 1
            
            for d, count in distances.items():
                if count == 2:
                    boomerangs += 2
                elif count > 2:
                    boomerangs += perm(count, 2)
            
        return boomerangs


from collections import Counter
class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0

        n = len(points)
        boomerangs = 0

        for (x1, y1) in points:
            distances = Counter()
            for (x2, y2) in points:
                d1 = (x2 - x1)
                d2 = (y2 - y1)
                d = sqrt(d1*d1 + d2* d2)
                distances[d] += 1
            
            for count in distances.values():
                boomerangs += (count * (count - 1)) # n * (n-1) ways
            
        return boomerangs



from collections import defaultdict
class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0

        n = len(points)
        boomerangs = 0

        for (x1, y1) in points:
            distances = defaultdict(int)
            for (x2, y2) in points:
                d1 = (x2 - x1)
                d2 = (y2 - y1)
                d = sqrt(d1*d1 + d2* d2)
                distances[d] += 1
            
            for count in distances.values():
                boomerangs += (count * (count - 1)) # n * (n-1) ways
            
        return boomerangs


from collections import defaultdict
class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0

        n = len(points)
        boomerangs = 0

        for (x1, y1) in points:
            distances = defaultdict(int)
            for (x2, y2) in points:
                d1 = (x2 - x1)
                d2 = (y2 - y1)
                distances[(d1*d1 + d2*d2)] += 1 # removing sqrt as we don't need it here
            
            for count in distances.values():
                boomerangs += (count * (count - 1)) # n * (n-1) ways
            
        return boomerangs