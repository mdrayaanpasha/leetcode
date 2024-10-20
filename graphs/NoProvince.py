class Solution(object):
    
    def DFS(self,M,N,V):
        V[N]=True
        lenght=len(M[N])

        for i in range(lenght):
            if M[N][i]==1 and not V[i]:
                self.DFS(M,i,V)
            
            

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        lenght=len(isConnected[0])
        count=0
        visited=[False]*lenght

        for i in range(lenght):
            if not visited[i]:
                count+=1
                self.DFS(isConnected,i,visited)
            

        return count
