class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = math.inf
        dp = [0] + [MAX] * amount
        
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return dp[amount] if dp[amount] != MAX else -1