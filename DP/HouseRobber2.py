class Solution(object):

    def helper(self,nums):
        n=len(nums)
        Acc = [0] * n


        for i in range(n):
            if i == 0 or i == 1:
                Acc[i]=nums[i]
            else:
                Acc[i]=nums[i]+max(Acc[:i-1])

        return max(Acc[n-1],Acc[n-2])
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        n=len(nums)
        if n == 1:
            return nums[n-1]
        return max(self.helper(nums[1:n]),self.helper(nums[0:n-1]))
        

        