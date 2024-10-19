from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adj_graph = [[] for _ in range(numCourses)]

        # creating adj matrix
        for a, b in prerequisites:
            adj_graph[a].append(b)
            in_degree[b] += 1
        
        in_degree_zero = deque(i for i, degree in enumerate(in_degree) if degree == 0)

        registered_courses = 0
        while in_degree_zero:
            course = in_degree_zero.popleft()
            registered_courses += 1

            for child in adj_graph[course]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    in_degree_zero.append(child)
        
        return numCourses == registered_courses
