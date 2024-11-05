class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        + APPROACH:
         - find the biggest pile.
         - create a range 1..max 
         - find a optimal # of B i can eat within h.
        
        + How to Opt?
         - start at mid and see if it can make you eat all B in h.
          -> if so then it means that its the min # of B you can eat 
             mid...right so take right=mid
          -> if not it means that dude this range left...mid cant take all B.
             so take left=mid+1
          -> return left or right (cause they meet at end :)

        + How to see if koko eats mid b per hour it can eat all b's?
         - well track hours=0
         - for every pile in piles.
            pile/mid is the hours it takes, eg pile =2 and mid=2 then it takes
            1 hour.

         - return true if hours < h else false
        """

        def canKokoEat(piles, k, h):
            TH = 0
            for pile in piles:
                TH += (pile + k - 1) // k 
            return TH <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if canKokoEat(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return left