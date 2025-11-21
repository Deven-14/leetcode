from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        queue = [(-count, task) for task, count in task_count.items()]
        heapq.heapify(queue)
        completed_tasks = 0

        while queue:
            cycle_completed_tasks = 0
            temp_queue = []
            min_tasks_to_complete = min(n + 1, len(queue))

            while cycle_completed_tasks < min_tasks_to_complete:
                count, task = heapq.heappop(queue)
                count += 1
                if count != 0:
                    temp_queue.append((count, task))
                cycle_completed_tasks += 1
            
            while temp_queue:
                heapq.heappush(queue, temp_queue.pop())
            
            completed_tasks += cycle_completed_tasks
            if queue and cycle_completed_tasks <= n:
                completed_tasks += n - cycle_completed_tasks + 1
                    
        return completed_tasks
    

from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        queue = [-count for task, count in task_count.items()]
        heapq.heapify(queue)
        completed_tasks = 0

        while queue:
            cycle_completed_tasks = 0
            temp_queue = []
            min_tasks_to_complete = min(n + 1, len(queue))

            while cycle_completed_tasks < min_tasks_to_complete:
                count = heapq.heappop(queue)
                count += 1
                if count != 0:
                    temp_queue.append(count)
                cycle_completed_tasks += 1
            
            while temp_queue:
                heapq.heappush(queue, temp_queue.pop())
            
            completed_tasks += cycle_completed_tasks
            if queue and cycle_completed_tasks <= n:
                completed_tasks += n - cycle_completed_tasks + 1
                    
        return completed_tasks


from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        
        max_freq = max(task_count.values())

        max_count = sum(freq == max_freq for freq in task_count.values())

        # Formula: (max_freq - 1) * (n + 1) + max_count
        # This fills (max_freq - 1) chunks of size (n + 1), then append max_count tasks
        max_freq_tasks_time = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), max_freq_tasks_time)