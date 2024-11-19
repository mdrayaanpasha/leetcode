class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        here its simple mate, so what you gotta do is compute the cost to jump at each postion and minimize it!
        classic DP. fuckin' Love it!!!
        """
        n = len(nums)
        dp = [float('inf')] * n  
        dp[0] = 0 

        for i in range(n):
            for c in range(1, nums[i] + 1): 
                if i + c >= n:
                    break
                dp[i + c] = min(dp[i + c], dp[i] + 1)  
        
        return dp[n - 1]


        