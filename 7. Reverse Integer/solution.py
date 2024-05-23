class Solution:
    def reverse(self, x: int) -> int:
        n = 2 ** 31

        x_abs_str = str(abs(x))
        x_abs_rev = x_abs_str[::-1]
        x_abs_len = len(x_abs_str)

        if x < 0:
            n_abs_min = n
            n_abs_min_str = str(n_abs_min)
            if (x_abs_len < len(n_abs_min_str) or x_abs_rev <= n_abs_min_str):
                return int("-" + x_abs_rev)
            else:
                return 0
        elif x > 0:
            n_abs_max = n-1
            n_abs_max_str = str(n_abs_max)
            if (x_abs_len < len(n_abs_max_str) or x_abs_rev <= n_abs_max_str):
                return int(x_abs_rev)
            else:
                return 0
        else:
            return 0
