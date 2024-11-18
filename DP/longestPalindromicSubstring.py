class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        => so heres the trick mate:

        - first check if boundars are equal.

        - then chekc if nonboundary are palindromes? via dp table.

        - but listen up there is a possibility that there can be even
          number of palindromes, so check for consequtive palindromes.
          i.e: s[i]==s[i+1]

        - then now see the loop thing is tricky!@#!@:
          + so the technique is start from finding the lenght of 
            palindromes.
          + so start from lenght = 3 to n. cause we chekced for 1 and 2 
            in base case.
          + then second loop go from 0...n-lenght+1, cause see last 
            lenght elements cant have combinations of lenght size.
          + then check for condition and voila you have the solution.
        """
        n=len(s)
        Max=1
        MaxIndex=(0,0)
        dp=[[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            MaxIndex=(i,i)
        
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                Max=2
                MaxIndex=(i,i+1)
                
                
        for l in range(3,n+1):
            for i in range(0,n-l+1):
                j=i+l-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    Max=max(Max,l)
                    MaxIndex=(i,j)
                    
                    
        
        return s[MaxIndex[0]:MaxIndex[1]+1]
        