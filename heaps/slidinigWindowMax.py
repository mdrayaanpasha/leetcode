class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        whats the plan phil???

        - so why not traverse normally and keep adding elements in the heap...
        - then always lets keep track of smallest number and see if its index is within the window
          assuming i is the right boundary.
        - then everytime after k steps keep adding min!!!
        """

        n = len(nums)
        r=k-1
        heap = []
        res=[]
        for i in range(n):
            heapq.heappush(heap,(-nums[i],i))


            while heap[0][1] < i-k+1:
                heapq.heappop(heap)

            
            if i>= k-1:
                res.append(-heap[0][0])

        return res

