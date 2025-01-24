class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for i in range(len(s)):
            if s[i] in map_t_s:
                if map_t_s[s[i]] != t[i]:
                    return False
                
            if t[i] in map_s_t:
                if map_s_t[t[i]] != s[i]:
                    return False

            map_t_s[s[i]] = t[i]
            map_s_t[t[i]] = s[i]


        return True

