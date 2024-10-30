class Solution(object):
    def maxOperations(self, nums, k):
        """
        How you doin'?
        - so the stratergy is to make a hash map.
        - key = nums[i], value=i
        - then run a loop.
        - target=k-nums[i], if target in hashMap then pop elements.
        """
        HashMap = {}
        counter=0

        for elem in nums:
            target=k-elem
            if HashMap.get(target,0) > 0:
                counter+=1
                HashMap[target]-=1
            else:
                HashMap[elem]=HashMap.get(elem,0) + 1

        return counter
                


        