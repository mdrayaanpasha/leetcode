class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        def binSearch(ele, arr):
            high,low = len(arr), 0
              
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < ele:
                    low=mid+1
                else:
                    high=mid
                 
            return low

        potions.sort()

        min_val = [(success + spell - 1) // spell for spell in spells]

        result=[]
        for mv in min_val:
            index=binSearch(mv, potions)
            result.append(len(potions)-index)
            
        return result