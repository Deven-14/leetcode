"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        def dfs(node, visited={}):
            if node.val in visited:
                return visited[node.val]

            new_node = Node(node.val)
            visited[node.val] = new_node

            new_neighbors = []
            for neighbor in node.neighbors:
                new_neighbor = dfs(neighbor, visited)
                new_neighbors.append(new_neighbor)
            
            new_node.neighbors = new_neighbors
            return new_node
        
        return dfs(node)


            