class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
         = = = = = = = = = = = = = = = = = = = STRATERGY = = = = = = = = = = = = = = = = = = = = 

          - S1: create 2 pointers, left and right \U0001f603
          
          - traverse thru the thing while adding and storing it \U0001f3c3

          - if that sum >= target -> then shrink the window by like l+=1 where l = left \U0001f914

          - keep track of sub-arrs whose sum is target BTW. \U0001fad9

         = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

        """

        # \U0001fad9 Track
        Min = float('inf')
        Sum=0
        l,r,n=0,0,len(nums)


        for r in range(n):
            Sum+=nums[r]

            while Sum >= target:
                Min=min(Min,r-l+1)
                Sum-=nums[l]
                l+=1


        return 0 if Min == float('inf') else Min




        

