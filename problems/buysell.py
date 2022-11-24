from ast import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        elif len(prices) == 1:
            return prices[0]

        l = 0
        r = 0

        # Move left whenever right is smaller
        # Right always moves right unless left moves
        diff = prices[r] - prices[l]
        while r < len(prices):
            diff = max(diff, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l += 1
            else:
                r += 1

        return diff
