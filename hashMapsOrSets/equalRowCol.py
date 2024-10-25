class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        new_dict = defaultdict(int)
        equal=0
        for column in grid:
            new_dict[tuple(column)]+=1
        n=len(grid)
        for c in range(n):
            check=tuple(grid[r][c] for r in range(n))
            if check in new_dict:
                equal+=new_dict[check]
                
                
        return equal