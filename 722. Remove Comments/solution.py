class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        program = "$".join(source)

        stack = []
        i = 0
        n = len(program)
        while program:
            j, k = program.find("//"), program.find("/*")
            if j == -1 and k == -1:
                stack.append(program)
                program = ""
            elif j != -1 and k != -1:
                if j < k:
                    end = program.find("$", j)
                    end = n if end == -1 else end
                    left, program = program[:j], program[end:]
                    stack.append(left)
                    i = end
                else:
                    end = program.find("*/", k+2)
                    left, program = program[:k], program[end+2:]
                    stack.append(left)
                    i = end + 3
            elif j == -1:
                end = program.find("*/", k+2)
                left, program = program[:k], program[end+2:]
                stack.append(left)
                i = end + 3
            else:
                end = program.find("$", j)
                end = n if end == -1 else end
                left, program = program[:j], program[end:]
                stack.append(left)
                i = end
            
        return [ele for ele in "".join(stack).split("$") if len(ele) != 0]
