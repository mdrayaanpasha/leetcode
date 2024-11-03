from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.pings=deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)

        while self.pings[0] < t - 3000:
            self.pings.popleft()


        return len(self.pings)

        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)