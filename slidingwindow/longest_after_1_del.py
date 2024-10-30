class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max=0
        Zeros=0
        LP=0
        
        for RP in range(len(nums)):
            if nums[RP] == 0:
                Zeros+=1
                
                while Zeros > 1:
                    if nums[LP] == 0:
                        Zeros-=1
                    LP+=1
                    
            Max=max(Max,RP-LP )
            
        return Max
    
    

        