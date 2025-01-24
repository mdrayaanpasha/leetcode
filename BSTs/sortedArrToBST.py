class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

     
        mid = len(nums)//2

        root = TreeNode(nums[mid])

        root.right = self.sortedArrayToBST(nums[mid+1:])
        root.left = self.sortedArrayToBST(nums[:mid])

        
        return root
        """
        WHATS THE PLAN PHIIIIIEEELLLL>?>??????

        - so notice you peice of shit the val in the root is the mid value.
            be it floor or ceil dont matter!!!!!
        - here's where it gets interesting you skunk, the right is again arr[:mid]'s middle!!
        - right is again the same: arr[mid:]'s middle val!!
        

        SO HOW TO SOLVE IT?????

        - go to freakin mid everytime with s,f stratergy!!!
        - 

        - why dont we make a recursive function that be like updating our children as recursively!!



        """
