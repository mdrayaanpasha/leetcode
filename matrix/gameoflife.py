class Solution:
    def gameOfLife(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        # WHATS THE PLAN PHIEEL????

            - claire ill create this function which will give 
               me live count.
            - if kill a cell if its livecount > 3 or < 2
            - ill make them alive if its livecount == 3 now.

            - but see this isnt async!!! this must be synch
              so we will have states if dead to alive then: 2
            - if alive to dead = 2

        """
        m=len(grid)
        n=len(grid[0])
        def liveCount(x,y):
            directions = [[-1,-1],[-1,0],[-1,1],
                          [0,-1],[0,1],
                          [1,-1],[1,0],[1,1]
                        ]
            count=0
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                
                if 0 <= nx < m and 0 <=  ny < n:
                    #see 1 is alive, and 3 is dead from alive,
                    #  but this was synchronous so!!
                    if grid[nx][ny] in (1,3):
                        count+=1
        

            return count


        for i in range(m):
            for j in range(n):
                lc = liveCount(i,j)
                if grid[i][j] == 1:
                    if lc > 3 or lc < 2:
                        grid[i][j]=3
                else:
                    if lc == 3:
                        grid[i][j]=2

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    grid[i][j]=1
                elif grid[i][j] == 3:
                    grid[i][j]=0

        

        
