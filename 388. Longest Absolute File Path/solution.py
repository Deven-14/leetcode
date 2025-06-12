class Solution:
    def lengthLongestPath(self, input: str) -> int:
        longest_absolute_path = 0
        directories = input.split("\n")
        n = len(directories)
        i = 0
        stack = []

        while i < n:
            item = directories[i]
            l = item.count("\t")

            while len(stack) > l:
                stack.pop()
            
            directory = item.removeprefix("\t" * l)
            stack.append(directory)

            is_file = "." in directory
            if is_file:
                longest_absolute_path = max(longest_absolute_path, len("/".join(stack)))
            
            i += 1
        
        return longest_absolute_path


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        longest_absolute_path = 0
        directories = input.split("\n")
        path_length = {0: 0}

        for line in directories:
            directory = line.lstrip("\t")
            depth = len(line) - len(directory)
            is_file = "." in directory

            if is_file:
                longest_absolute_path = max(longest_absolute_path, path_length[depth] + len(directory))
            else:
                path_length[depth + 1] = path_length[depth] + len(directory) + 1 # +1 for '/'
                    
        return longest_absolute_path


