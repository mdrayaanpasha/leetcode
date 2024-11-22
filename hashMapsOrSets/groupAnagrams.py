class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        - stratergy well its simple, take a string sort it and keep it as a key in your dict.
        - ps: i tried ascii it didnt work 🥲
        """
        res=[]
        D = defaultdict(list)
        
        for s in strs: #O(n)
            k=tuple(sorted(s)) #O(s log s)
            D[k].append(s)

        #so: O(n * s log s)
        for val in D.values(): 
            res.append(val)

        return res
            