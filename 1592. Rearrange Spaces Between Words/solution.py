class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        n = len(words)
        count = text.count(" ")
        if n == 1:
            if count == 0:
                return text
            return words[0] + " " * count

        max_adj_space, end_space = divmod(count, n - 1)
        return (" " * max_adj_space).join(words) + " " * end_space