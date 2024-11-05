class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Alright mate so the intuition is, to take my mid to peak by pushing it to a number such that its greater then anything in front of it, cause i     wanna keep pushing it, then once im at this point then wallah, just move my righ to this peak and were done.
        
        """
        
        left,right=0,len(nums)-1

        while left < right:
            mid=(left+right)//2

            if nums[mid] < nums[mid+1]:
                left=mid+1
            else:
                right=mid

        return left