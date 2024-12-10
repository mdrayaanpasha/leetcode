class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        ======================STRATERGY========================
        - This looks like a bad boy but really isnt.
        - so first we need to perform rotation meaning reverese 
          last k elements
        - then bring them somehow to the begining k elements.
        - but imagine this i have to 12 rotations and size of my arr
          is 5, then we reverese it twice it becomes usual then we are
          left with 2 rotations. so this can be done with modulo 
          arithematic.
        - then just perform arr ops

        """

        n=len(nums)
        k=k%n

        nums[:]=nums[-k:]+nums[:-k]



        

