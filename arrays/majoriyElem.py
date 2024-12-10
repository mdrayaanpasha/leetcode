from collections import Counter
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Dict = Counter(nums)

        maj = math.ceil(len(nums) / 2)

        for key,val in Dict.items():
            if val >= maj:
                return key
        
