class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        - well now this is what you call interesting! 🤌
        - we init 4 boundaries l,r,t,b.
        - then we run a loop that runs until l < r and t < b.
        - append in this order: l-r -> t-b -> r-l -> b-t.
        - do this and make sub problems for which this loop solves without recursion BTW :)

        """

        l,r=0,len(matrix[0])
        t,b=0,len(matrix)
        res=[]
        
        
        while l < r and t < b:
            #left to right
            for i in range(l,r):
                res.append(matrix[t][i])
            t+=1
            
            #top to bottom
            for i in range(t,b):
                res.append(matrix[i][r-1])
            r-=1
            
            #once u do this check if its not a row or col matrix.
            # if so -> dude break we are done, else nah bro run those spirals
            if not (l < r and t < b):
                break
            
            #right to left
            for i in range(r-1,l-1,-1):
                res.append(matrix[b-1][i])
            b-=1
            
            #bottom to top
            for i in range(b-1,t-1,-1):
                res.append(matrix[i][l])
            l+=1
            
        
        return res