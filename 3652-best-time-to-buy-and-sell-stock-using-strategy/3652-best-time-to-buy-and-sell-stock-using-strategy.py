from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        m = k // 2
        
        # Baseline profit
        A = [strategy[i] * prices[i] for i in range(n)]
        base = sum(A)
        
        # Sliding window to compute best delta for one modification
        sumA = sum(A[:k])
        sumP2 = sum(prices[m:k])  # prices of the second half for window starting at 0
        bestDelta = sumP2 - sumA
        
        for l in range(1, n - k + 1):
            # Update sum of A over the whole window [l, l+k-1]
            sumA += A[l + k - 1] - A[l - 1]
            # Update sum of prices over the second half [l+m, l+k-1]
            sumP2 += prices[l + k - 1] - prices[l + m - 1]
            cur = sumP2 - sumA
            if cur > bestDelta:
                bestDelta = cur
        
        if bestDelta < 0:
            bestDelta = 0
        
        return base + bestDelta

# b886d7f8-0d10-4db8-87e4-9661fa53b2f0