import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        so the technique is simple what you gotta do is like maintain
        - first convert all edges to graph.
        - then run dijkstra on it, but ensure you only append those edges whose weight
          has been updated.
        - maintain a heapq and ensure that this your poping the element with highest pr
          each time.

        """
        G = {i:[] for i in range(n)}
        
        for i,(u,v) in enumerate(edges):
            G[u].append((v,succProb[i]))
            G[v].append((u,succProb[i]))

        Prob = [0 for i in range(n)]
        Prob[start]=0
        pq=[(-1,start)]
        while pq:
            wei,node=heapq.heappop(pq)
            wei=-wei

            if node == end:
                return wei

            for nei, neiWei in G[node]:
                new_wei=wei*neiWei

                if new_wei > Prob[nei]:
                    Prob[nei]=new_wei
                    heapq.heappush(pq,(-new_wei,nei))
        

        return 0
