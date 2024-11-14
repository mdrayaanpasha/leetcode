class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <=2:
            return n
        else:
            table=[0] * (n+1)
            table[1],table[2]=1,2
        
            
            for i in range(3,n+1):
                table[i]=table[i-1]+table[i-2]

        return table[n]
        