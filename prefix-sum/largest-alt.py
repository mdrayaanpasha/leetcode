class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        Max=Alt=0
    
        for elem in gain:
            Alt+=elem
            Max=max(Max,Alt)
            
        return Max
        