class Solution:

    def balanced_brackets(self, s):
        bracket_pairs = {}
        open_stack = []

        for i, char in enumerate(s):
            if char == "[":
                if open_stack:
                    open_stack[-1] = (open_stack[-1][0], True)
                open_stack.append((i, False))

            elif char == "]":
                open_bracket_idx, has_sub_brackets = open_stack.pop()
                bracket_pairs[open_bracket_idx] = (i, has_sub_brackets)
        
        return bracket_pairs
        
    def helper(self, s, bracket_pairs, i, j):
        if i > j:
            return ""
        
        if not s[i].isnumeric():
            if s[i] == "]":
                return self.helper(s, bracket_pairs, i + 1, j)
            return s[i] + self.helper(s, bracket_pairs, i + 1, j)

        open_bracket_idx = s.find("[", i+1)

        k = int(s[i:open_bracket_idx])

        closed_bracket_idx, has_sub_brackets = bracket_pairs[open_bracket_idx]
        
        if not has_sub_brackets:
            t1 = k * s[open_bracket_idx + 1 : closed_bracket_idx]
            t2 = self.helper(s, bracket_pairs, closed_bracket_idx + 1, j)
            return t1 + t2

        t1 = k * self.helper(s, bracket_pairs, open_bracket_idx + 1, closed_bracket_idx)
        t2 = self.helper(s, bracket_pairs, closed_bracket_idx + 1, j)

        return t1 + t2

    def decodeString(self, s: str) -> str:
        bracket_pairs = self.balanced_brackets(s)
        return self.helper(s, bracket_pairs, 0, len(s)-1)



class Solution:

    def balanced_brackets(self, s):
        bracket_pairs = {}
        open_stack = []

        for i, char in enumerate(s):
            if char == "[":
                if open_stack:
                    open_stack[-1] = (open_stack[-1][0], True)
                open_stack.append((i, False))

            elif char == "]":
                open_bracket_idx, has_sub_brackets = open_stack.pop()
                bracket_pairs[open_bracket_idx] = (i, has_sub_brackets)
        
        return bracket_pairs
        
    def helper(self, s, bracket_pairs, i, j):
        if i > j:
            return ""
        
        if not s[i].isnumeric():
            if s[i] == "]":
                return self.helper(s, bracket_pairs, i + 1, j)
            return s[i] + self.helper(s, bracket_pairs, i + 1, j)

        open_bracket_idx = s.find("[", i+1)
        k = int(s[i:open_bracket_idx])
        closed_bracket_idx, has_sub_brackets = bracket_pairs[open_bracket_idx]
        
        if not has_sub_brackets:
            t1 = k * s[open_bracket_idx + 1 : closed_bracket_idx]
        else:
            t1 = k * self.helper(s, bracket_pairs, open_bracket_idx + 1, closed_bracket_idx)
        
        t2 = self.helper(s, bracket_pairs, closed_bracket_idx + 1, j)
        return t1 + t2

    def decodeString(self, s: str) -> str:
        bracket_pairs = self.balanced_brackets(s)
        return self.helper(s, bracket_pairs, 0, len(s)-1)



class Solution:

    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
                continue
            
            sub_string = ""
            while stack and stack[-1] != "[":
                sub_string = stack.pop() + sub_string
            
            stack.pop() # "["

            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            
            stack.append(int(num) * sub_string)
        
        return "".join(stack)


