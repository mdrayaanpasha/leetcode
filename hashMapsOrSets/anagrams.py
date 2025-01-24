from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        DictS = Counter(s)
        DictT = Counter(t)

        for key,val in DictT.items():
            if DictT[key] != DictS[key]:
                return False

        return True
