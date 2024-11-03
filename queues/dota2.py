class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        St = list(senate)
        RQ = deque()
        DQ = deque()
        
        
        for i,c in enumerate(St):
            if c=='R':
                RQ.append(i)
            else:
                DQ.append(i)
                
        
        while RQ and DQ:
            RI=RQ.popleft()
            DI=DQ.popleft()
            
            if RI > DI:
                DQ.append(DI + len(St))
            
            if DI > RI:
                RQ.append(RI + len(St))
                
                
        return "Radiant" if RQ else  "Dire"
        