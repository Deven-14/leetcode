from collections import Counter
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        str_counts = Counter(strs)
        non_lus_strs = { string for string in str_counts if str_counts[string] > 1 }
        lus_strs = { string for string in str_counts if str_counts[string] == 1 }

        def is_subsequence(string1, string2):
            l1, l2 = len(string1), len(string2)
            k = l1 - l2
            diff = 0
            i, j = 0, 0
            while diff <= k and j < l2:
                if string1[i] != string2[j]:
                    i += 1
                    diff += 1
                else:
                    i += 1
                    j += 1
            
            return diff <= k
        

        def is_subsequence_of_non_lus(string):
            for non_lus_str in non_lus_strs:
                if len(non_lus_str) <= len(string):
                    continue
                if is_subsequence(non_lus_str, string):
                    return True
            
            return False
        
        for string in sorted(lus_strs, key=len, reverse=True):
            if not is_subsequence_of_non_lus(string):
                return len(string)
        
        return -1



from collections import Counter
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        str_counts = Counter(strs)
        non_lus_strs = { string for string in str_counts if str_counts[string] > 1 }
        lus_strs = { string for string in str_counts if str_counts[string] == 1 }

        def is_subsequence(string1, string2):
            # check if string2 is subsequence of string1
            it = iter(string1)
            return all(c in it for c in string2)
        

        def is_subsequence_of_non_lus(string):
            for non_lus_str in non_lus_strs:
                if len(non_lus_str) <= len(string):
                    continue
                if is_subsequence(non_lus_str, string):
                    return True
            
            return False
        
        for string in sorted(lus_strs, key=len, reverse=True):
            if not is_subsequence_of_non_lus(string):
                return len(string)
        
        return -1
            


            