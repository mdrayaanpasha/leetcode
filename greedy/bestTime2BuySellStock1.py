class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        Min=float('inf')
        Max=0

        for p in prices:
            if p < Min:
                Min = p
            if p - Min > Max:
                Max = p - Min


        return Max
        
