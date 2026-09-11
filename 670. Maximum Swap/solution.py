class Solution:
    def maximumSwap(self, num: int) -> int:
        queue = deque()
        str_num = str(num)
        for i, n in enumerate(str_num):
            while queue and str_num[queue[-1]] <= n:
                queue.pop()
            queue.append(i)
        
        swap_idx = -1
        for i, n in enumerate(str_num):
            if i >= queue[0]:
                queue.popleft()
            if queue and n < str_num[queue[0]]:
                swap_idx = i
                break
        
        if swap_idx == -1:
            return num
        
        str_num_list = list(str_num)
        str_num_list[swap_idx], str_num_list[queue[0]] = str_num_list[queue[0]], str_num_list[swap_idx]

        return int("".join(str_num_list))