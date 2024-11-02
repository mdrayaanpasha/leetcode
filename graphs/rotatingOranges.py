class Solution(object):
    def orangesRotting(self, grid):
        from collections import deque

        """
        #SOLVE THIS LIKE: 
        - find rotten oranges first and them in your Queue.
        - Counter = 0
        - dequeue and traverse 4Directionally and see if its 1. if so then enqueue.
        - atlast after adding all neighbors, counter+=1
        - do this until Q is not Empty.
        - return counter if counter > 0 else -1
        
        """
        Q=deque()
        FO=M=0
        D=[(0,1),(0,-1),(1,0),(-1,0)]

        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    FO+=1
                if grid[i][j] == 2:
                    Q.append((i,j))
        if FO == 0:
            return 0          
        while Q:
            M+=1
            for _ in range(len(Q)):
                x,y=Q.popleft()
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny]=2
                        FO-=1
                        Q.append((nx,ny))
                        
                        
        return M-1 if FO == 0 else -1
    
    
                
    
    
        