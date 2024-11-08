import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap=[]

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap,num)
            else:
                heapq.heappop(heap)


        return heap[0]

        