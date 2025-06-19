from collections import defaultdict
from itertools import chain

class DisjointSetUnion:

    def __init__(self, variables):
        self.parents = { var: var for var in variables }
        self.rank = { var: 0 for var in variables }
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        
        px = self.parents[x]
        ppx = self.parents[px]
        if ppx == px:
            return px
        
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.rank[pv] < self.rank[pu]:
            u, v = v, u
            pu, pv = pv, pu
        
        self.rank[pu] += self.rank[pv]
        self.parents[pv] = pu

    def is_disjoint(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        return True


class Solution:

    def dfs(self, adj, node, target, visited=None):
        if visited is None:
            visited = set()
        
        if node == target:
            return True, 1.0
        
        for adj_node in adj[node]:
            if (node, adj_node) in visited:
                continue
            
            visited.add((node, adj_node))
            found, value = self.dfs(adj, adj_node, target, visited)
            if not found:
                continue
            
            return True, adj[node][adj_node] * value
        
        return False, 0.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        variables = set(chain.from_iterable(equations))
        dsu = DisjointSetUnion(variables)
        
        for (var1, var2), value in zip(equations, values):
            adj[var1][var2] = value
            adj[var2][var1] = 1 / value
            dsu.union(var1, var2)
        
        answers = []
        for var1, var2 in queries:
            if var1 not in variables or var2 not in variables or dsu.is_disjoint(var1, var2):
                answers.append(-1)
                continue
            
            _, value = self.dfs(adj, var1, var2)
            answers.append(value)
                
        return answers
            



from collections import defaultdict
from itertools import chain

class DisjointSetUnion:

    def __init__(self, variables):
        self.parents = { var: var for var in variables }
        self.rank = { var: 0 for var in variables }
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        
        px = self.parents[x]
        ppx = self.parents[px]
        if ppx == px:
            return px
        
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.rank[pv] < self.rank[pu]:
            u, v = v, u
            pu, pv = pv, pu
        
        self.rank[pu] += self.rank[pv]
        self.parents[pv] = pu

    def is_disjoint(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        return True


class Solution:

    def dfs(self, adj, node, target, visited=None):
        if visited is None:
            visited = set()
        
        if node == target:
            return 1.0
        
        for adj_node in adj[node]:
            if (node, adj_node) in visited:
                continue
            
            visited.add((node, adj_node))
            value = self.dfs(adj, adj_node, target, visited)
            if value == -1.0:
                continue
            
            return adj[node][adj_node] * value
        
        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        variables = set(chain.from_iterable(equations))
        dsu = DisjointSetUnion(variables)
        
        for (var1, var2), value in zip(equations, values):
            adj[var1][var2] = value
            adj[var2][var1] = 1 / value
            dsu.union(var1, var2)
        
        answers = []
        for var1, var2 in queries:
            if var1 not in variables or var2 not in variables or dsu.is_disjoint(var1, var2):
                answers.append(-1)
                continue
            
            value = self.dfs(adj, var1, var2)
            answers.append(value)
                
        return answers
            

# * removing True or false in dfs as values are between 0.0 < values[i] <= 20.0
# * because of the -1 in the dfs now, we won't even need dsu, but it makes it faster 
# * as we don't need to go through the entire tree to identify if doesn't exist and then assign value -1


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        equations_to_values = { tuple(eq): value for eq, value in zip(equations, values) }
        for (a, b), value in zip(equations, values):
            equations_to_values[(b, a)] = 1 / value
        
        divisions = defaultdict(set)

        for numerator, denominator in equations:
            divisions[numerator].add(denominator)
            divisions[denominator].add(numerator)

        def dfs(qn, qd, visited):
            if qn not in divisions:
                return -1
            
            if qd in divisions[qn]:
                return equations_to_values[(qn, qd)]
            
            visited.add(qn)
            for denominator in divisions[qn]:
                if denominator not in visited and (v := dfs(denominator, qd, visited)) > -1:
                    return equations_to_values[(qn, denominator)] * v
            
            return -1
        
        answers = []
        for qn, qd in queries:
            answers.append(dfs(qn, qd, set()))
        
        return answers