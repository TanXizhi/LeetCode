class Solution1:
    def maxProfit(self, prices: list[int]) ->int:
        curPrice = prices[0]
        maxProf = 0
        n = len(prices)
        for i in range(1,n):
            if prices[i] <= curPrice:
                curPrice = prices[i]
            else:
                maxProf = max(maxProf, prices[i]-curPrice)
        return maxProf

class Solution2:
    def maxProfit(self, prices: list[int]) ->int:
        minPrice = 1e10
        maxProf = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProf = max(maxProf, price - minPrice)
        return maxProf
