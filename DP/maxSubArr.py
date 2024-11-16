class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
        n=len(nums)
    
        GlobalMax=float('-inf')
        CurrentMax = 0
        
        for i in range(n):
            CurrentMax = max(nums[i],CurrentMax+nums[i])  
            GlobalMax = max(GlobalMax,CurrentMax)
                    
                    
        return GlobalMax