class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr=[[0] * _ for _ in range(1,n+1)]
    
        for i in range(n):
            for j in range(i+1):
                if j == 0 or j==i:
                    arr[i][j]=1
                else:
                    arr[i][j]=arr[i-1][j]+arr[i-1][j-1]

                    
                    
        return arr
        