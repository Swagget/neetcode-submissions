class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_time = 0
        sell_time = 0
        i = 0
        max_profit = 0
        current_profit = 0

        while i < len(prices):
            current_profit = prices[i] - prices[buy_time]
            if current_profit > max_profit:
                max_profit = current_profit
                sell_time = i
            if prices[i] < prices[buy_time]:
                buy_time = i
            i += 1
        return max_profit