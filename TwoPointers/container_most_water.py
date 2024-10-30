class Solution(object):
    def maxArea(self, height):
        LP=Max=0
        RP=len(height)-1
        
        while LP < RP:
            
            
            """
                area=height*width.
                - so height must be the min of both of the heights.
                - and width is the distance b/w lp and rp, i.e: RP-LP
            """
        
            curr_area=min(height[LP],height[RP]) * (RP-LP)
            Max=max(Max,curr_area)
            
            if height[LP] < height[RP]:
                LP+=1
            else:
                RP-=1
                
        
        return Max
        