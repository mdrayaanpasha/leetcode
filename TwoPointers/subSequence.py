class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Slist=list(s)
        Tlist=list(t)

        pointer=0
        n=len(Slist)

        for elem in Tlist:
            if pointer < n and Slist[pointer]==elem:
                pointer+=1

            if pointer == n:
                return True

            
        return pointer==n