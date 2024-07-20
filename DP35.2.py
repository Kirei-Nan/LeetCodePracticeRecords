class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp=[[0]*4 for _ in range(len(prices))]
        dp[0][0]=-prices[0]
        dp[0][2]=-prices[0]

        for i in range(len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i])  # 第一次持有
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])  # 第一次不持有
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])  # 第二次持有
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])  # 第二次不持有
        return dp[-1][3]