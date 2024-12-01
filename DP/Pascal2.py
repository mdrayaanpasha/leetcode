class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        PT =[[1] * (rows+1) for rows in range(rowIndex+1)]
    
        for i in range(2,(rowIndex+1)):
            for j in range(0,len(PT[i])):
                if j == 0 or j==len(PT[i])-1:
                    continue
                else:
                    PT[i][j]=PT[i-1][j]+PT[i-1][j-1]
                    print(PT[i][j])
                
        return PT[rowIndex]
        
