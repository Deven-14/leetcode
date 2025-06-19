class Solution:
    def toLowerCase(self, s: str) -> str:
        new_s = [
            chr(v + 32) if 65 <= (v := ord(char)) <= 90 else char
            for char in s
        ]
        return "".join(new_s)