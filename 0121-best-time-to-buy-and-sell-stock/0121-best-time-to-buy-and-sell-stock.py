class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        cur_profit = 0
        for idx in range(len(prices)-1):
            profit = prices[idx+1] - prices[idx]
            cur_profit += profit
            if cur_profit > max_profit:
                max_profit = cur_profit
            
            if cur_profit < 0:
                cur_profit = 0
        
        return max_profit        
            
            