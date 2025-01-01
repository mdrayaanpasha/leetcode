"""
 == ==  == SO HERE IS THE GAME == == ==

 - so we are distributing candies to kids.
 - each kid should get atleast one candy.
 - but kid gets more candy then its neighbor given they have more rating.

 - so you see each kid have 2 neighbors given they aren't edges.
 - if so then, first lets go from left to right. and give one candy more then neighbor:
   -> that is dist[i]=dist[i-1]+1
 - then lets go thru the right to left and increase candies by neighbors:
   - how increase?
     -> increase means, candies_dist > candies_dist to neigh
     -> if already more dont increment, else increment.


"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        #base case: 1 candy per kid.
        dist = [1] * n

        #left to right distro:
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                dist[i]=dist[i-1] + 1

        #right to left:
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                dist[i] = max(dist[i],dist[i+1] + 1)

        return sum(dist) 

        
        
     
