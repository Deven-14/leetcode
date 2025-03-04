class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        sub_seq = [words[0]]

        for i in range(1, len(words)):
            if groups[i] ^ groups[i-1]: # or !=
                sub_seq.append(words[i])

        return sub_seq