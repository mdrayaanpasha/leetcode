class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = sum(nums[:k])
        max_avg = current_sum / float(k)
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            new_avg = current_sum / float(k)
            max_avg = max(new_avg, max_avg)
                
        return max_avg