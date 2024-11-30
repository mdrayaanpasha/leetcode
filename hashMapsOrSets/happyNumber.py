class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashSet=set() #created a hashset!
        temp=n
        while True:
            S=0
            while temp != 0:
                
                S+= (temp%10) ** 2
                temp=temp//10
                
            
            if S in hashSet:
                return False
            if S == 1:
                return True
            
            hashSet.add(S)
            temp=S
            
        return S
        
