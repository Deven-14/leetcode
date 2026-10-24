class Solution:
    def maximumTime(self, time: str) -> str:
        return "".join([
            time[0] if time[0] != '?' else ("2" if time[1] == "?" or time[1] <= "3" else "1"),
            time[1] if time[1] != '?' else ("3" if time[0] in "2?" else "9"),
            ":",
            time[3] if time[3] != '?' else "5",
            time[4] if time[4] != '?' else "9",
        ])