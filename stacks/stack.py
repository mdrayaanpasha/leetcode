class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize=maxSize
        self.Arr = [0] * maxSize
        self.Top=-1
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.Top < self.maxSize - 1:
            self.Top+=1
            self.Arr[self.Top]=x


        

    def pop(self):
        """
        :rtype: int
        """
        if self.Top < 0:
            return -1

        self.Top-=1
        return self.Arr[self.Top+1]
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """

        limit = min(k,self.Top+1)
              
        for i in range(limit):
            self.Arr[i]+=val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
