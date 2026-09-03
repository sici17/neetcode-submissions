class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit=0

        for p in range(len(prices)-1):
            diff=prices[p+1]-prices[p]
            if(diff>0):
                profit+=diff
        
        return profit

        