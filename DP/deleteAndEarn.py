class Solution(object):
    def deleteAndEarn(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        Freq=Counter(n)
        Max_Num = max(n)
        dp = [0] * (Max_Num + 1)
        for num in range(1,Max_Num+1):
            dp[num] = max((num * Freq[num]) + dp[num-2], dp[num-1])
            
            
        return dp[Max_Num]
