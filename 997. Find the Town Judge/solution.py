class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a_b_trust = defaultdict(set)
        b_a_trust = defaultdict(set)

        for p1, p2 in trust:
            a_b_trust[p2].add(p1)
            b_a_trust[p1].add(p2)
        
        rem = n-1
        for i in range(1, n+1):
            if len(a_b_trust[i]) == rem and i not in b_a_trust:
                return i
        
        return -1


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a_b_trust = defaultdict(int)
        b_a_trust = defaultdict(int)

        for p1, p2 in trust:
            a_b_trust[p2] += 1
            b_a_trust[p1] += 1
        
        rem = n-1
        for i in range(1, n+1):
            if a_b_trust[i] == rem and i not in b_a_trust:
                return i
        
        return -1


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a_b_trust = defaultdict(int)
        b_a_trust = defaultdict(int)

        for p1, p2 in trust:
            a_b_trust[p2] += 1
            b_a_trust[p1] += 1
        
        rem = n-1
        for i in range(1, n+1):
            if i not in b_a_trust and a_b_trust[i] == rem:
                return i
        
        return -1


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a_b_trust = [0] * (n + 1)
        b_a_trust = [0] * (n + 1)

        for p1, p2 in trust:
            a_b_trust[p2] += 1
            b_a_trust[p1] += 1
        
        rem = n-1
        for i in range(1, n+1):
            if b_a_trust[i] == 0 and a_b_trust[i] == rem:
                return i
        
        return -1


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a_b_trust = [0] * (n + 1)

        for p1, p2 in trust:
            a_b_trust[p2] += 1 # Person p2 is trusted → moves toward being judge
            a_b_trust[p1] -= 1 # p1 trusts someone, disqualifies them from being judge
        
        rem = n-1
        for i in range(1, n+1):
            if a_b_trust[i] == rem:
                return i
        
        return -1


