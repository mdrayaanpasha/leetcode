class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
    
  
        paperCount = [0] * (n + 1)
        
        for elem in citations:
            paperCount[min(elem, n)] += 1
        
        h=n
        papers = paperCount[n]
        
        while papers < h:
            h-=1
            papers+=paperCount[h]
            
        return h
        
