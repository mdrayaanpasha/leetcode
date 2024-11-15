class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


        n=len(nums)
        TS = sum(nums)
        
        if TS % 2 != 0:
            return False
        target = TS // 2
        DP = [False] * (target+1)
        DP[0] = True

        # [1,5,11,5]
        for num in nums:
            #11,10,9,8,7,6,5,4,3,2,1
            for i in range(target,num-1,-1):
                DP[i]=DP[i] or DP[i-num]

        return DP[target]


       
        