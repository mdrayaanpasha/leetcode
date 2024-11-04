# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=0
        end=n
        

        while True:
            pick=random.randint(start,end)
            ans=guess(pick)
            if ans == -1:
                end=pick-1
            elif ans == 1:
                start=pick+1
            else:
                return pick
            
            pick=random.randint(start,end)
        