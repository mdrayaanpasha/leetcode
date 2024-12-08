class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,n=0,len(nums)

        while i < n:
            if nums[i] != val:
                i+=1
            else:
                nums[i]=nums[n-1]
                n-=1

        return i
