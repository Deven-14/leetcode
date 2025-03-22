class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_map = dict(knowledge)
        chars = []

        i, n = 0, len(s)
        while i < n:
            if s[i] == "(":
                j = s.find(")", i+1)
                key = s[i + 1:j]
                value = knowledge_map.get(key, "?")
                chars.append(value)
                i = j + 1

            else:
                chars.append(s[i])
                i += 1
        
        return "".join(chars)


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_map = dict(knowledge)
        s_split_on_open = s.split('(')

        sub_strings = [s_split_on_open[0]]
        for i in range(1, len(s_split_on_open)):
            key, sub_string = s_split_on_open[i].split(')')
            sub_strings.append(knowledge_map.get(key, "?"))
            sub_strings.append(sub_string)
        
        return "".join(sub_strings)

