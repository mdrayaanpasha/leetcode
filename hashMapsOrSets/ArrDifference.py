class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1=set(nums1)
        set2=set(nums2)

        unset1=set1-set2
        unset2=set2-set1

        return [list(unset1),list(unset2)]