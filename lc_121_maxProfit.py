class Solution:
  #动态规划，二维数组非常慢，直接用贪心会快很多
    def maxProfit(self, prices: List[int]) -> int:
        row, col = 2, len(prices)
        dp = [[0] * col for _ in range(row)]

        dp[0][0] = 0
        dp[1][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1]+prices[i])
            dp[1][i] = max(dp[1][i-1], -prices[i])
        return dp[0][len(prices)-1]
