class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        TS=sum(nums)
        LS=RS=0

        for i in range(len(nums)):
            RS=TS-LS-nums[i]

            if RS == LS:
                return i

            LS+=nums[i]

        return -1
        