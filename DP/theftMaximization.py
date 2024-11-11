class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        AccumlatedMoney=[0]*n
        for i in range(n):
            if i == 0 or i==1:
                AccumlatedMoney[i]=nums[i]
            else:
                AccumlatedMoney[i]=nums[i] + max(AccumlatedMoney[:i-1])
                
        
        return max(AccumlatedMoney[n-1],AccumlatedMoney[n-2])
            