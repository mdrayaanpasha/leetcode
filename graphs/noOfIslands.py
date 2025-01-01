class Solution:
    """
    WHATS THE PLAN PHEEL!@#>

    - so why dont i traverse thru the adjacency freking matrix.
    - then if i see a 1, add # of island+=1 and then, mark all 
      parts of this island to be 0 with dfs traversal.

    - HOW DFS IS AUGMENTED?

     + so you traverse, you always always make that node = 0, then 
       call dfs on up, right,left, down.
    + but see im calling dfs to every right, so sometimes it 
      can go beyond boundary or call a 0th elem, so return in 
      that case. 
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ISLAND=0
        m,n=len(grid),len(grid[0])

        def dfs(i,j):

            #now lets check out base case.
            if i < 0 or j < 0 or j >= n or i >= m or grid[i][j]!="1":
                return
            grid[i][j]='0'
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ISLAND+=1


        return ISLAND
