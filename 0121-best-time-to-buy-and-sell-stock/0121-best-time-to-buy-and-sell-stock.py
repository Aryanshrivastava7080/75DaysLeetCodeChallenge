class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        prft = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            prft = max(prft, p - buy_price)
        
        return prft