class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        LP,RP=0,0
        Sorted=[]
        while LP < m and RP < n:
            if nums1[LP] <= nums2[RP]:
                Sorted.append(nums1[LP])
                LP+=1
            else:
                Sorted.append(nums2[RP])
                RP+=1
                
        while LP < m:
            Sorted.append(nums1[LP])
            LP+=1
        
        while RP < n:
            Sorted.append(nums2[RP])
            RP+=1
            
        for i in range(m+n):
            nums1[i]=Sorted[i]
