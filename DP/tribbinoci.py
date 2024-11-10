class Solution(object):
    def __init__(self):
        self.DP=[0,1,1]
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(self.DP) > n:
            return self.DP[n]
        else:
            for i in range(len(self.DP),n+1):
                self.DP.append(self.DP[i-1]+self.DP[i-2]+self.DP[i-3])


            return self.DP[n]
        