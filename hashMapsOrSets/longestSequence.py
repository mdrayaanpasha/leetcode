class Solution:
    """
    # So stratergy is awesome!
    - How to about this you make a hash set of arr for O(1)
    - ok now only loop thru the series of elem if there isn't 
      a num B4 this.
    - Cause u see if its there then starting from here isnt gonna 
      be the longest.
    - so lets start from there and loop thru.
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        Max = 0
        S = set(nums)

        for ele in S:
            if ele-1 not in S:
                streak=1
                num=ele

                while num+1 in S:
                    streak+=1
                    num+=1

                Max=max(Max,streak)

        return Max
       
