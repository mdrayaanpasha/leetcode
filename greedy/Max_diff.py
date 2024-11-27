class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        Max_diff=0
        Min_val=arrays[0][0]
        Max_val=arrays[0][-1]


        for arr in arrays[1:]:
            Max_diff=max(Max_diff,abs(arr[-1]-Min_val),abs(arr[0]-Max_val))
            
            Min_val=min(Min_val,arr[0])
            Max_val=max(Max_val,arr[-1])


        return Max_diff
        