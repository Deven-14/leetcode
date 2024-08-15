class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            tank = gas[i]
            gas_to_travel = cost[i]
            if tank < gas_to_travel:
                continue
            
            tank = tank - gas_to_travel
            j = (i+1) % n
            tank += gas[j]
            gas_to_travel = cost[j]
            while j != i and tank >= gas_to_travel:
                tank = tank - gas_to_travel
                j = (j+1) % n
                tank += gas[j]
                gas_to_travel = cost[j]
            
            if j == i:
                return j
        
        return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        pre = [0] * n
        pre[0] = gas[0] - cost[-1]
        for i in range(1, n):
            pre[i] = gas[i] - cost[i-1]

        for i in range(n):
            tank = gas[i]
            gas_to_travel = cost[i]
            if tank < gas_to_travel:
                continue
            
            j = (i+1) % n
            tank += pre[j]
            while j != i and tank >= cost[j]:
                j = (j+1) % n
                tank += pre[j]
            
            if j == i:
                return j
        
        return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        i = 0
        n = len(gas)
        while i < n:
            tank = gas[i]
            gas_to_travel = cost[i]
            if tank < gas_to_travel:
                i += 1
                continue
            
            start_index = i
            j = i + 1
            while j < n and tank >= gas_to_travel:
                tank = tank - gas_to_travel + gas[j]
                gas_to_travel = cost[j]
                j += 1
            
            i = j
            
        return start_index


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        tank = 0
        start_index = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start_index = i+1
        
        return start_index