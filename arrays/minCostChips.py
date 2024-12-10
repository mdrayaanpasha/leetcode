class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """

        STRATERGY:

        - fun actually, so first find the number of even elems and odd 
          elems
        - you see moving all odd to one index or moving all even to one
          index costs 0 bucks.
        - so now we want to see after moving all of them to one index, 
          all odd in one place all even in one place. adjacent to each 
          other is a perfect intution.
        - then select a stack either even or odd one which ever is min 
        """

        EvenCount=sum(1 for p in position if p % 2 == 0)
        OddCount = len(position)-EvenCount

        return min(EvenCount,OddCount)
        
