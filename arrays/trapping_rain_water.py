class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0 

        acc = 0 
        n = len(height)
        LP, RP = 0, n - 1
        Lmax, Rmax = height[LP], height[RP]

        while LP < RP:
            if Lmax < Rmax:
                LP += 1
                acc += max(0, Lmax - height[LP])
                Lmax = max(Lmax, height[LP])
            else:
                RP -= 1
                acc += max(0, Rmax - height[RP])
                Rmax = max(Rmax, height[RP])

        return acc

