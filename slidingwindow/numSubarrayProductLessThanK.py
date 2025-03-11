class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int


        SAME STORY I HAD A THING:
        where i used to like count stuff in 2 loops n^2 TBH

        which was like ill keep on adding product until my product bcomes greater then k.
        but ineff adn doesnt work!!!


        Thanks to Mr. GPT, made my life easy agina!!!!


        so how about we keep on expanding our window from left to right!!!

        if the product of stuff is >  then ill keep on shrinking !!!

        add increment the # of sub-arr evertime...

        so right-left is the # of sub array's there must exist!!!




        """
        n=len(nums)
        counter=0
        left = 0 
        p=1
        for right in range(n):
            p*=nums[right]

            while p >= k and left <= right:
                p //= nums[left]
                left+=1

            counter+=(right-left+1)

        
        return counter
