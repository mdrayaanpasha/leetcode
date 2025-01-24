class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
       
        here i am maximizing the # of intervals i g
        .. how? cause imagine if i had like sorted
        them in ascending order, then it would mean
        that one of them might end soon one late, but
        here evey one ends in sorted order, so
        maximize the # of intervals.
        
        why maximize the # of intervals?
        - cause we want to minimize the # of deletions.
        
        """
        n=len(intervals)
        count=0
        intervals.sort(key=lambda x:x[1])
        prev = intervals[0][1]
        print(intervals)
        
        for i in range(1,n):
            if prev > intervals[i][0]:
                count+=1
            else:
                prev = intervals[i][1]
                
                
        return count
