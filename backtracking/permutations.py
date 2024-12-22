class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """

        WHATS THE PLAN :) ??

        - so why dont we keep adding stuff linearly, until it 
          reaches size = n = len(nums).
        - so only add those nums everytime which we aren't part of 
          of the sol array already!!
        """

        ans,sol = [],[]
        n=len(nums)

        def backtrack():
            if n == len(sol):
                ans.append(sol[:])
                return

            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
            
            
        backtrack()
        return ans
