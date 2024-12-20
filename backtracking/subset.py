class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        """
         WHATS THE PLAN PHEEIL??#!#

         - so i learnt this new thing today, descions tree
         - so am like with every event i have descion to take i can 
           take it or leave it.
        - and then if i keep doing this for all at my leaf of descion
          trees i'll have all possible scenarios that could have happend
          with all combinations of descions.

        - IN GENERAL WE HAVE A BASE CASE TO STOP AT, A DESCION TO TAKE 
          AND NOT TAKE.

        - SO WHILE ITERATING OVER THE ELEMS, I'LL ADD BOTH SCENARIOS
        ADDING AND NOT ADDING THE CURR ELEM.

        """

        n=len(nums)
        sol,res=[],[]

        def helper(i):

            #base case:
            if i == n:
                res.append(list(sol))
                return

            #take it.
            sol.append(nums[i])
            helper(i+1)
            sol.pop()

            #dont take it
            helper(i+1)
        helper(0)
        return res

            
        
