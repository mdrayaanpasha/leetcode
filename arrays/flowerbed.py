class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        NP=0
        lenght=len(flowerbed)
        for i in range(lenght):
            if NP != n:
                if flowerbed[i]==0:
                    leftEmpty=(i==0) or (flowerbed[i-1]==0)
                    rightEmpty=(i==lenght-1) or (flowerbed[i+1]==0)
                    
                    if leftEmpty and rightEmpty:
                        NP+=1
                        flowerbed[i]=1
            else:
                break
        return NP==n
