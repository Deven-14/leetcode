import heapq
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        unique_chars = set(s)
        unique_sub_seqs = []
        unique_sub_seq = []
        unique_sub_seq_set = set()

        def helper(i):
            if len(unique_sub_seq) == len(unique_chars):
                unique_sub_seqs.append("".join(unique_sub_seq))
                return
            
            for j in range(i, n):
                if s[j] in unique_sub_seq_set:
                    continue
                
                unique_sub_seq_set.add(s[j])
                unique_sub_seq.append(s[j])
                helper(j+1)
                unique_sub_seq.pop()
                unique_sub_seq_set.remove(s[j])
        
        helper(0)
        return min(unique_sub_seqs)


# timed out

import heapq
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_indices = [0] * 26
        ord_a = ord('a')
        char_index = lambda char: ord(char) - ord_a
        
        for i, char in enumerate(s):
            last_indices[char_index(char)] = i
        
        stack = []
        visited = [False] * 26
        for i, char in enumerate(s):
            idx = char_index(char)
            if visited[idx]:
                continue
            
            while stack and char < stack[-1] and last_indices[char_index(stack[-1])] > i:
                visited[char_index(stack.pop())] = False
            
            stack.append(char)
            visited[idx] = True
        
        return "".join(stack)

            
import heapq
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_indices = {char: i for i, char in enumerate(s)}
        stack = []
        visited = dict.fromkeys("abcdefghijklmnopqrstuvwxyz", False)

        for i, char in enumerate(s):
            if visited[char]:
                continue
            
            while stack and char < stack[-1] and last_indices[stack[-1]] > i:
                visited[stack.pop()] = False
            
            stack.append(char)
            visited[char] = True
        
        return "".join(stack)
