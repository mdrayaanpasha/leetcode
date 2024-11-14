class Solution(object):
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """


        if n == 0 or n == 1:
            return n
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n]=self.fib(n-1) + self.fib(n-2)
            return self.memo[n]