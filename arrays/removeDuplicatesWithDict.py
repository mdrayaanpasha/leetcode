from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        Dict = Counter(nums)
    
        for i,(key,val) in enumerate(Dict.items()):
            nums[i]=key
            
        print(nums)

        return len(Dict)
        
