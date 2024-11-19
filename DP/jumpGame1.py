class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        + here the strategy is simple: 
        + from here check whats the max i can reach?
        + ask 2 questions:
        + am i at the postion where i cant reach the max: i > most.
        + if yes -> return False.
        + then check if fromhere i add a jump, can i reach the end?
        + if yes -> return True. else at last return False.
         
        """
        most=0
        n=len(nums)
        for i in range(n):
            if i > most:
                return False
            else:
                most=max(most,i+nums[i])
                if most >= n-1:
                    return True
                
           
        return False
        