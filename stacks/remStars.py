class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        SArr=list(s)
        Result=[]
        
    
        for i in range(len(SArr)):
            if SArr[i]=='*' and Result:
                Result.pop()
            else:
                Result.append(SArr[i])
                
        return "".join(Result)