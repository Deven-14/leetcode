class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        curr_width = 0
        for char in s:
            curr_width += widths[ord(char) - 97]
            if curr_width > 100:
                lines += 1
                curr_width = widths[ord(char) - 97]
        
        return [lines, curr_width]


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        curr_width = 0
        widths_map = { char: width for char, width in zip('abcdefghijklmnopqrstuvwxyz', widths)}
        for char in s:
            curr_width += widths_map[char]
            if curr_width > 100:
                lines += 1
                curr_width = widths_map[char]
        
        return [lines, curr_width]


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        curr_width = 0
        
        for char in s:
            w = widths[ord(char) - 97]
            curr_width += w
            if curr_width > 100:
                lines += 1
                curr_width = w
        
        return [lines, curr_width]