import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        
        left,right=0,len(costs)-1
        l_a,r_a=[],[]
        t_c,hires=0,0

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(l_a,costs[left])
                left+=1
            if left <= right:
                heapq.heappush(r_a,costs[right])
                right-=1

            
        while hires < k:
            if l_a and r_a:
                if l_a[0] <= r_a[0]:
                    t_c+=heapq.heappop(l_a)
                    if left <= right:
                        heapq.heappush(l_a,costs[left])
                        left+=1
                else:
                    t_c+=heapq.heappop(r_a)
                    if left <= right:
                        heapq.heappush(r_a,costs[right])
                        right-=1
            elif l_a:
                t_c+=heapq.heappop(l_a)
                if left <= right:
                    heapq.heappush(l_a,costs[left])
                    left+=1
            else:
                t_c+=heapq.heappop(r_a)
                if left <= right:
                    heapq.heappush(r_a,costs[right])
                    right-=1


            hires+=1

        return t_c