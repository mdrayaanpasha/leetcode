class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        stratergy its simple:
         - ill sell today if:
            prices today is greater then yesterday and ill accumulate it, 
            why dp when you have greedy!!!
        """

        profit=0
        n=len(prices)

        for i in range(1,n):
            if prices[i] > prices[i-1]:
                profit+=prices[i]-prices[i-1]


        return profit
        
