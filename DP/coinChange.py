class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        so the trick is DP forme.

        - me be i'll make a dp arr and be like dp[i] is min of itself or
          c being the coin we are currently focusing on, if dp[i-coin] +  1
        - and remember this thing its gonna add the values lke this:
        dp[1]=1 
        dp[2]=dp[2-1] + 1. (1 being the current num iterating over in a loop)

          cause one is the cost of taking coin and i-coin is the target coin.

        """

        dp= [float('inf')] * (amount+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin]+1)

            
        return dp[amount] if dp[amount] != float('inf') else -1
        