class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        we have ab int arr -> nums, and k, return true.
        if there are two distinct indices i and j in arr, s.t nums[i] == nums[j] 
        """

        index_map = {}

        for i,elem in enumerate(nums):
            if not elem in index_map:
                index_map[elem] = i
            elif i- index_map[elem] <= k:
                return True
            else:
                index_map[elem]=i

        return False 
        
