from itertools import groupby
class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed_chars = 0
        i = 0

        for key, group in groupby(chars):
            l = len(list(group))
            compressed_chars += 1
            chars[i] = key
            i += 1

            if l > 1:
                len_count = len(str(l))
                compressed_chars += len_count
                chars[i : i+len_count] = str(l)
                i += len_count
        
        return compressed_chars