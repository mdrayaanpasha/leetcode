class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        mcost=[0] * n
        
        for i in range(n):
            if i == 0 or i==1:
                mcost[i] = cost[i]
            else:
                mcost[i]=min(mcost[i-1]+cost[i],mcost[i-2]+cost[i])
                
        
                
        return min(mcost[n-1],mcost[n-2])