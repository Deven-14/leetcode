class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_list = [""] * len(s)
        for i, index in enumerate(indices):
            s_list[index] = s[i]
        return "".join(s_list)
        