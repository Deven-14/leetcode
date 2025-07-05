from itertools import groupby
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_group = [(k, len(list(g))) for k, g in groupby(name)]
        typed_group = [(k, len(list(g))) for k, g in groupby(typed)]

        if len(name_group) != len(typed_group):
            return False
        
        for i in range(len(name_group)):
            name_char, name_char_count = name_group[i]
            typed_char, typed_char_count = typed_group[i]

            if name_char != typed_char or name_char_count > typed_char_count:
                return False
        
        return True


# * can also be done with 2 pointers