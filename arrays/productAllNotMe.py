class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product=1
        zeroCount=0
        for i in range(len(nums)):
            if nums[i]!=0:
                product*=nums[i]
            else:
                zeroCount+=1
                
        if zeroCount > 1:
            return [0] * len(nums)
        elif zeroCount == 0:
            return [product/elem for elem in nums]
        else:
            return [product if elem==0 else 0 for elem in nums]