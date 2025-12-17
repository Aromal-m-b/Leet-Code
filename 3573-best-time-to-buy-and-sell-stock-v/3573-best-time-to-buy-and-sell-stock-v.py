from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0

        k = min(k, n // 2)
        NEG_INF = -10**18

        dp0 = [NEG_INF] * (k + 1)
        dpL = [NEG_INF] * (k + 1)
        dpS = [NEG_INF] * (k + 1)
        dp0[0] = 0

        for price in prices:
            new_dp0 = dp0[:] 
            new_dpL = dpL[:] 
            new_dpS = dpS[:]

            for t in range(k):
                if dp0[t] != NEG_INF:
                    if dp0[t] - price > new_dpL[t]: 
                        new_dpL[t] = dp0[t] - price
                    if dp0[t] + price > new_dpS[t]: 
                        new_dpS[t] = dp0[t] + price

            for t in range(k):
                if dpL[t] != NEG_INF:
                    profit = dpL[t] + price  
                    if profit > new_dp0[t + 1]:
                        new_dp0[t + 1] = profit
                if dpS[t] != NEG_INF:
                    profit = dpS[t] - price
                    if profit > new_dp0[t + 1]:
                        new_dp0[t + 1] = profit

            dp0, dpL, dpS = new_dp0, new_dpL, new_dpS

        return max(dp0)