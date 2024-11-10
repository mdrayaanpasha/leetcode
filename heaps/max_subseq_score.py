import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        pairs=[(n1,n2) for n1,n2 in zip(nums1,nums2)]
        pairs=sorted(pairs,key=lambda x:x[1], reverse=True)

        minheap=[]
        Sum=0
        Max=0

        for n1,n2 in pairs:
            Sum+=n1
            heapq.heappush(minheap,n1)

            

            if len(minheap) > k:
                Sum-=heapq.heappop(minheap)

            if len(minheap) == k:
                Max=max(Max,Sum*n2)

            
        return Max
        