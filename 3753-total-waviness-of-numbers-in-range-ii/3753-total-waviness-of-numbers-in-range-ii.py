from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(limit: int) -> int:
            if limit <= 0:
                return 0

            digits = list(map(int, str(limit)))

            @cache
            def dp(pos, prev2, prev1, started, tight):
                if pos == len(digits):
                    return (1, 0)  # (count, waviness)

                upper = digits[pos] if tight else 9

                total_count = 0
                total_wave = 0

                for d in range(upper + 1):
                    ntight = tight and (d == upper)

                    # Still skipping leading zeros
                    if started == 0 and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            -1,
                            -1,
                            0,
                            ntight
                        )

                    # First significant digit
                    elif started == 0:
                        cnt, wav = dp(
                            pos + 1,
                            -1,
                            d,
                            1,
                            ntight
                        )

                    # Second significant digit
                    elif started == 1:
                        cnt, wav = dp(
                            pos + 1,
                            prev1,
                            d,
                            2,
                            ntight
                        )

                    # We already have at least two digits
                    else:
                        add = 0

                        if (
                            (prev1 > prev2 and prev1 > d)
                            or
                            (prev1 < prev2 and prev1 < d)
                        ):
                            add = 1

                        cnt, wav = dp(
                            pos + 1,
                            prev1,
                            d,
                            2,
                            ntight
                        )

                        wav += add * cnt

                    total_count += cnt
                    total_wave += wav

                return (total_count, total_wave)

            return dp(0, -1, -1, 0, True)[1]

        return solve(num2) - solve(num1 - 1)