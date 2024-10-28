class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numZeros=0
        l=0
        m_s=0
        n=len(nums)

        for r in range(n):
            if nums[r] == 0:
                numZeros+=1
            #this is  like unfucking all the zeros i fucked of window at size: nums[l:r]. this will remove only one of your fucked up thing, i.e extra.
            while numZeros > k:
                if nums[l]==0:
                    numZeros-=1

                l+=1

            w=r-l+1
            m_s=max(m_s,w)


        return m_s


            
        