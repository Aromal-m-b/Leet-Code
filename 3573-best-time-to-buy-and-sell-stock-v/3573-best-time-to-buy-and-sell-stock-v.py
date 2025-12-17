class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[0] * 3 for _ in range(k + 1)] for _ in range(n)]
        for transaction_count in range(1, k + 1):
            dp[0][transaction_count][1] = -prices[0]
            dp[0][transaction_count][2] = prices[0]
        for day in range(1, n):
            for transaction_count in range(1, k + 1):
                dp[day][transaction_count][0] = max(
                    dp[day - 1][transaction_count][0],                    
                    dp[day - 1][transaction_count][1] + prices[day],      
                    dp[day - 1][transaction_count][2] - prices[day]      
                )
                dp[day][transaction_count][1] = max(
                    dp[day - 1][transaction_count][1],                             
                    dp[day - 1][transaction_count - 1][0] - prices[day]            
                )
                dp[day][transaction_count][2] = max(
                    dp[day - 1][transaction_count][2],                              
                    dp[day - 1][transaction_count - 1][0] + prices[day]           
                )
        return dp[n - 1][k][0]