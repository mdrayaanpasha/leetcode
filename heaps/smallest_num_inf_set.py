import heapq
class SmallestInfiniteSet(object):

    def __init__(self):
        self.AddedItems=set()
        self.minHeap=[]
        self.currentSmallest=1

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.minHeap:
            s=heapq.heappop(self.minHeap)
            self.AddedItems.remove(s)
            return s
        s=self.currentSmallest
        self.currentSmallest+=1
        return s

        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.AddedItems and num < self.currentSmallest:
            self.AddedItems.add(num)
            heapq.heappush(self.minHeap,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)