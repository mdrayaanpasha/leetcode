from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        heap = []
        for key,val in counter.items():
            heapq.heappush(heap,(-val,key))

        return [heapq.heappop(heap)[1] for _ in range(k)] 
        
