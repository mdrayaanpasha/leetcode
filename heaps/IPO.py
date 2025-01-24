import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int

        WHATS THE PLAN PHIIEEEEL!!!!!?

        - so what if i could min heapify the captials, such that i get minimum capital to work with.
        - now that i have it how about? traversing thru each capital index, and see if the project was solvable within this?
          if so then ill take it!!
        """

        heap = [(num,i) for i,num in enumerate(capital)]

        heapq.heapify(heap)
        profs = []
        for _ in range(k):

            while heap and heap[0][0] <= w:
                elem,i = heapq.heappop(heap)
                heapq.heappush(profs,-profits[i])

            if not profs:
                break

            
            w += -heapq.heappop(profs)


        return w

            

        
        
