"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {employee.id: employee for employee in employees}
        importance = emp[id].importance

        def dfs(emp_id):
            importance = 0
            for sub in emp[emp_id].subordinates:
                importance += emp[sub].importance
                importance += dfs(sub)
            
            return importance
        
        importance += dfs(id)
        return importance


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {employee.id: employee for employee in employees}
        importance = emp[id].importance

        queue = deque(emp[id].subordinates)
        while queue:
            sub_id = queue.popleft()
            importance += emp[sub_id].importance
            queue.extend(emp[sub_id].subordinates)
                    
        return importance



"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {employee.id: employee for employee in employees}

        def dfs(emp_id):
            importance = emp[emp_id].importance
            for sub in emp[emp_id].subordinates:
                importance += dfs(sub)
            return importance
        
        return dfs(id)


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {employee.id: employee for employee in employees}

        def dfs(emp_id):
            e = emp[emp_id]
            importance = e.importance
            for sub in e.subordinates:
                importance += dfs(sub)
            return importance
        
        return dfs(id)


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {employee.id: employee for employee in employees}
        importance = 0

        stack = [id]
        while stack:
            e = emp[stack.pop()]
            importance += e.importance
            stack.extend(e.subordinates)
                    
        return importance


    