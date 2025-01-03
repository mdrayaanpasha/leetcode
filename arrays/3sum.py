class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        STRATERGY IS SIMLPLE:

        - find inverse of all possible pairs let they be non duplicates
        """

        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,h = i+1, n-1


            while l < h:

                Sum = nums[i]+nums[l]+nums[h]

                if Sum == 0:
                    res.append([nums[i],nums[l],nums[h]])
                    l+=1
                    h-=1

                    while l < h and nums[l] == nums[l-1]:
                        l+=1
                    while l < h and nums[h] == nums[h+1]:
                        h-=1

                elif Sum > 0:
                    h-=1
                else:
                    l+=1

        return res
            
                

