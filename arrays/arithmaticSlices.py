class Solution(object):
    
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Initial plan was to like make an iterative window thing where ill keep on increasing the 
        size of window and then count all the diff adn increment on a count, but boy that was 
        expensive!!! it was O(n^3)...

        so i gotta O(n) now!!! (thanks to mr. gpt)

        - firstly start a window of size of 3, then do the differnce in one iteration of all of
          them.
        - if difference was like gud, gud then move on increase the size of window if bad, bad,
          then -> ++ count to whatever you had and decrement the no of stuff possible to 0.
        """
        
        n = len(nums)

        if n < 3:
            return 0

        Counter=0
        TotalCounter=0
        for i in range(2,n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                Counter+=1
                TotalCounter+=Counter

            else:
                Counter=0





        return TotalCounter
