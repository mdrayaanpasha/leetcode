class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict1={}
        for elem in arr:
            if elem not in dict1:
                dict1[elem]=1
            else:
                dict1[elem]+=1
            
        newdict={}
        
        for keys,vals in dict1.items():
            if vals not in newdict:
                newdict[vals]=keys
            else:
                return False
            
        return True
        

