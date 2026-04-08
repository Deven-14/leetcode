from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)

        while counts:
            n = groupSize
            ele = min(counts)

            while n and counts[ele] > 0:
                counts[ele] -= 1
                if counts[ele] == 0:
                    del counts[ele]
                n -= 1
                ele += 1

            if n != 0:
                return False

        return True


from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counts = Counter(hand)

        for ele in hand:
            if counts[ele] == 0:
                continue
            
            n = groupSize
            while n and counts[ele] > 0:
                counts[ele] -= 1
                if counts[ele] == 0:
                    del counts[ele]
                n -= 1
                ele += 1

            if n != 0:
                return False

        return True
    

from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counts = Counter(hand)

        for ele in hand:
            if counts[ele] == 0:
                continue
            
            n = groupSize
            while n and counts[ele] > 0:
                counts[ele] -= 1
                n -= 1
                ele += 1

            if n != 0:
                return False

        return True


from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)

        for ele in sorted(counts):
            if counts[ele] == 0:
                continue
            
            n = groupSize
            k = counts[ele]
            while n and counts[ele] >= k:
                counts[ele] -= k
                n -= 1
                ele += 1

            if n != 0:
                return False

        return True


