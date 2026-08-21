from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        # Remove redundant coins
        coins.sort()
        filtered = []

        for coin in coins:
            if not any(coin % prev == 0 for prev in filtered):
                filtered.append(coin)

        coins = filtered
        n = len(coins)

        def lcm(a, b):
            return a * b // gcd(a, b)

        # Count numbers <= x divisible by at least one coin
        def count(x):
            total = 0

            # Generate every non-empty subset
            for mask in range(1, 1 << n):

                current_lcm = 1
                selected_count = 0

                # Get the actual coin denomination
                # corresponding to every enabled bit
                for i in range(n):
                    if mask & (1 << i):
                        selected_count += 1

                        current_lcm = lcm(
                            current_lcm,
                            coins[i]
                        )

                        # No multiple can contribute
                        if current_lcm > x:
                            break

                divisible_count = x // current_lcm

                # Odd number of selected coins -> add
                if selected_count % 2 == 1:
                    total += divisible_count

                # Even number of selected coins -> subtract
                else:
                    total -= divisible_count

            return total


        # Binary search for kth number
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left