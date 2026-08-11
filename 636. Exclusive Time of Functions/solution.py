class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exec_times = [0] * n

        for log in logs:
            func, state, timestamp = log.split(":")
            func = int(func)
            timestamp = int(timestamp)
            if state == "start":
                stack.append([timestamp, 0])
            else:
                start_timestamp, wait_time = stack.pop()
                exec_time = timestamp - start_timestamp + 1
                exec_times[func] += exec_time - wait_time
                if stack:
                    stack[-1][1] += exec_time
            
        return exec_times


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exec_times = [0] * n
        prev_time = 0

        for log in logs:
            func, state, timestamp = log.split(":")
            func = int(func)
            timestamp = int(timestamp)
            if state == "start":
                if stack:
                    exec_times[stack[-1]] += timestamp - prev_time
                stack.append(func)
                prev_time = timestamp
            else:
                exec_times[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
            
        return exec_times


