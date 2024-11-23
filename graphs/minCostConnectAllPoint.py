class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #lets convert it into an adj list.
        N=len(points)
        adj = {i:[] for i in range(N)}

        for i in range(N):
            xi,yi=points[i]
            for j in range(i+1,N):
                xj,yj=points[j]
                dist=abs(xi-xj)+abs(yi-yj)
                adj[i].append([dist,j])
                adj[j].append([dist,i])


        '''
        - so now that i have this adj list, i wanna run prims on it.
        - so have a minheap to store edges with min weight.
        - run dfs by poppins minheap nodes.

        '''
        visit=set()
        minH=[[0,0]]
        res=0

        '''
        - Trick here is simple, alright so i keep adding nodes of those elements which i havent 
          visited yet
        
        - and if i store it in a minheap, then acess smallest distance in O(1), so i pop the min 
          elem, see if its visited, if vis -> continue its gone from list. else you will get the 
          min of the node which you havent visited yet.


        '''
        while len(visit) < N:
            cost,node=heapq.heappop(minH)

            if node in visit:
                continue

            res+=cost
            visit.add(node)

            for neighborCost, neighbor in adj[node]:
                if neighbor not in visit:
                    heapq.heappush(minH,[neighborCost,neighbor])

        return res