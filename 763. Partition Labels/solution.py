class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = { char: i for i, char in enumerate(s) }
        substring_start_idx = -1
        substring_end_idx = -1
        substrings = []

        for i, char in enumerate(s):
            substring_end_idx = max(substring_end_idx, last_idx[char])
            if i == substring_end_idx:
                substrings.append(substring_end_idx - substring_start_idx)
                substring_start_idx = substring_end_idx
        
        return substrings
