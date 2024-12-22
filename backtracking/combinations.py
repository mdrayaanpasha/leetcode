class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        STRATERGY!

        - so i'll start picking from reverse, i'll be like:
        - dont pick unless what you will get if keep picking from 
          now is > what i need, pick when its equal. 
        - also pick in other side of tree which you can stop when
          you get the of size you want it to be in.
        """


        ans,sol = [],[]

        def backtrack(x):
            if len(sol) == k:
                ans.append(list(sol))
                return


            left = x
            need = k - len(sol)

            if left > need:
                backtrack(x-1)

            sol.append(x)
            backtrack(x-1)
            sol.pop()

        backtrack(n)
        return ans
        
